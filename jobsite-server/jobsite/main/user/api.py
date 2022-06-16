#from django.http import HttpResponse
#from urllib.request import Request
#from django.shortcuts import render
#from django.urls import path
#from django.views.decorators.csrf import csrf_protect, csrf_exempt

import json
from django.utils import timezone
from django.core import serializers

from google.oauth2 import id_token
from google.auth.transport import requests

import traceback

#from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

import datetime
#import random

from .model import User
from .serializer import UserSerializer, UserFullSerializer
from .utils import generate_access_token, generate_refresh_token

from ..utils import Utils

# Create your views here.

class LoginGoogle(APIView):
    #authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    def response_login(self, user: User, request):
        res = Response('user.token')
        serializer_context = {
            'request': request,
        }
        serialized_user = UserSerializer(user, context=serializer_context)

        res.data = {
            'access_token': user.token,
            'user': serialized_user.data,
        }
        return res

    def insert_user(self, info):
        user = User()
        user.first_name = info['given_name']
        user.last_name = info['family_name']
        user.username = user.last_name + ' ' + user.first_name
        user.password = Utils.random_hex(128)
        user.joined_date = datetime.datetime.now()
        user.social_account_id = info['sub']
        user.social_account = info['email']
        user.social_auth_iss = info['iss']

        # to get user id
        user.save()

        user.token, user.token_expires = generate_access_token(user)
        user.save()

        return user


    def post(self, request):       
        try:
            idinfo = id_token.verify_oauth2_token(request.data['credential'], requests.Request(), 
                request.data['clientId'], 3000)

            gID = idinfo['sub']

            user: User = User.objects.get(social_account_id=gID)

            if (user.social_auth_iss != idinfo['iss'] 
                or user.social_account != idinfo['email']):
                return Response('Something went wrong!')

            if (user.token_expires < timezone.now()):
                user.token, user.token_expires = generate_access_token(user)
                user.save()

            return self.response_login(user, request)

        except User.DoesNotExist:
            return self.response_login(self.insert_user(idinfo), request)
            #return Response('OK')
        except ValueError:
            traceback.print_exc()
            return Response('Failed to login!')
    

class TestAuth(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user: User = request.user
        return Response(Utils.model_to_dict(user))
        