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
import hashlib

#from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

import datetime

from ..company.models import Company
from ..employee.models import Employee
from ..employer.models import Employer

from .model import User, UserRole, UserRoleRelationship
from .serializer import UserSerializer, UserFullSerializer
from .utils import generate_access_token, generate_refresh_token

from ..utils import Utils

from .role import RoleID

# Create your views here.

class LoginGoogle(APIView):
    #authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    def response_login(self, user: User, request):
        res = Response()
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
        


class Registration(APIView):
    authentication_classes = []
    permission_classes = []

    def insert_user(self, username, password, email):
        user = User()
        #user.first_name = 'NULL'
        #user.last_name = 'NULL'
        user.username = username
        user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user.joined_date = datetime.datetime.now()
        #user.social_account_id = info['sub']
        user.social_account = email
        #user.social_auth_iss = info['iss']

        # to get user id
        user.save()

        user.token, user.token_expires = generate_access_token(user)
        user.save()

        return user

    def post(self, request):
        user_name = request.data['username']
        password = request.data['password']
        email = request.data['email']

        print(request.data)

        try:
            User.objects.get(username=user_name)
            return Response('User name exists', status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user = self.insert_user(user_name, password, email)

            serializer_context = {
                'request': request,
            }
            serialized_user = UserSerializer(user, context=serializer_context)

            data = {
                'access_token': user.token,
                'user': serialized_user.data,
            }

            return Response(data, status.HTTP_200_OK)


class Login(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user_name = request.data['username']
        password = request.data['password']

        users = User.objects.filter(username=user_name)

        if not users.exists():
            return Response('User name not found', status.HTTP_400_BAD_REQUEST)

        user: User = users.first()
        inputPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if inputPassword != user.password:
            return Response('Password incorrect', status.HTTP_400_BAD_REQUEST)

        if (user.token_expires < timezone.now()):
            user.token, user.token_expires = generate_access_token(user)
            user.save()

        res = Response()
        serializer_context = {
            'request': request,
        }
        serialized_user = UserSerializer(user, context=serializer_context)
        res.data = {
            'access_token': user.token,
            'user': serialized_user.data,
        }
        return res


class SetRole(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user: User = request.user
        role: str = request.data['role_id']
        roleId = int(role)

        rels = UserRoleRelationship.objects.filter(user=user.id)

        for r in rels.iterator():
            if r.user_role.id == roleId:
                return Response('Role exists', status.HTTP_400_BAD_REQUEST)

        try:
            if roleId == RoleID.EMPLOYEE:
                UserRoleRelationship.objects.create(user=user, user_role=UserRole.objects.get(id=roleId))
                Employee.objects.create(user=user)

            elif roleId == RoleID.EMPLOYER:
                company_id = request.data['company_id']
                Employer.objects.create(user=user, company=Company.objects.get(id=company_id))
                UserRoleRelationship.objects.create(user=user, user_role=UserRole.objects.get(id=roleId))
                
            else:
                return Response('Admin role', status.HTTP_400_BAD_REQUEST)

        except:
            traceback.print_exc()
            return Response('Fatal error', status.HTTP_400_BAD_REQUEST)

        return Response('Done')