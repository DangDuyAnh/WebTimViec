import json
from django.utils import timezone
from django.core import serializers

import traceback
import hashlib

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status

from ..utils import Utils

from .models import ChatRoom, ChatRoomConversation, ChatRoomUser
from ..user.model import User
from ..user.serializer import UserSerializer

from django.db import connections

class CreatePair(APIView):
    #permission_classes = [IsAuthenticated]
    #authentication_classes = []
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user: User = request.user

        user_id2 = request.data['user_id']
        users = User.objects.filter(id=user_id2)

        if not users.exists():
            return Response('Recv user not found', status.HTTP_400_BAD_REQUEST)

        user2: User = users.first()
        
        chat_room_name = request.data['room_name']
        
        if ChatRoom.objects.filter(name=chat_room_name).exists():
            return Response('Chat room duplicate', status.HTTP_400_BAD_REQUEST)

        chat_room: ChatRoom = ChatRoom()
        chat_room.name = chat_room_name
        chat_room.save()

        chat_room_user = ChatRoomUser()
        chat_room_user.user = user
        chat_room_user.room = chat_room
        chat_room_user.save()

        chat_room_user2 = ChatRoomUser()
        chat_room_user2.user = user2
        chat_room_user2.room = chat_room
        chat_room_user2.save()

        return Response(Utils.model_to_dict(chat_room))


def IsUserBelongToRoom(user: User, room: ChatRoom) -> bool:
    return ChatRoomUser.objects.filter(user=user, room=room).exists()

class Send(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user: User = request.user

        room_id = request.data['room_id']
        room: ChatRoom = ChatRoom.objects.get(id=room_id)

        chat_room_users_ = ChatRoomUser.objects.filter(user=user, room=room)

        if not chat_room_users_.exists():
            return Response('User must belong to room', status.HTTP_400_BAD_REQUEST)


        #chat_room_users: ChatRoomUser = chat_room_users_.first()
        #conversation: ChatRoomConversation = ChatRoomConversation()
        #conversation.sender_user = chat_room_users
        #conversation.room = chat_room_users
        #conversation.text = request.data['text']
        #conversation.save()
        cursor = connections['default'].cursor()
        text = request.data['text']
        cursor.execute(f'INSERT INTO `chat_room_conversation` (`sender_user_id`, `room_id`, `text`) VALUES({user.id}, {int(room_id)}, \'{text}\')')

        return Response('Done')


class Conversation(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user: User = request.user
        room_id = request.query_params['room_id']
        room: ChatRoom = ChatRoom.objects.get(id=room_id)

        #chat_room_users: ChatRoomUser = ChatRoomUser.objects.filter(user=user, room=room)

        if not IsUserBelongToRoom(user, room):
            return Response('User must belong to room', status.HTTP_400_BAD_REQUEST)

        convs = ChatRoomConversation.objects.filter(room_id=room_id)
        return Response(Utils.query_set_to_list(convs))


class List(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user: User = request.user

        chat_room_users_ = ChatRoomUser.objects.filter(user=user)
        if not chat_room_users_.exists():
            return Response({})

        arr = []
        for chat_room_user in chat_room_users_.iterator():
            #chat_room_user: ChatRoomUser
            arr.append(
                chat_room_user.room.id
            )
        
        return Response(arr)
        

class MembersList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user: User = request.user
        room_id = request.query_params['room_id']
        room: ChatRoom = ChatRoom.objects.get(id=room_id)

        if not IsUserBelongToRoom(user, room):
            return Response('User must belong to room', status.HTTP_400_BAD_REQUEST)

        chat_room_users_ = ChatRoomUser.objects.filter(room=room)
        if not chat_room_users_.exists():
            return Response({})

        arr = []
        for chat_room_user in chat_room_users_.iterator():
            #chat_room_user: ChatRoomUser
            arr.append(
                chat_room_user.user.id
            )
        
        return Response(arr)


class MembersDetailList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user: User = request.user
        room_id = request.query_params['room_id']
        room: ChatRoom = ChatRoom.objects.get(id=room_id)

        if not IsUserBelongToRoom(user, room):
            return Response('User must belong to room', status.HTTP_400_BAD_REQUEST)

        chat_room_users_ = ChatRoomUser.objects.filter(room=room)
        if not chat_room_users_.exists():
            return Response({})

        arr = []
        for chat_room_user in chat_room_users_.iterator():
            chat_room_user: ChatRoomUser
            arr.append(
                UserSerializer(chat_room_user.user, context={'request': request}).data
            )
        
        return Response(arr)