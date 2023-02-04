import json
import os
from django.utils import timezone
from django.core import serializers

import traceback
import hashlib

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status

from ..utils import Utils

from ..user.model import User
from ..user.serializer import UserSerializer

from django.db import connections

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
FINE_TUNED_MODEL = "davinci:ft-personal-2023-02-04-07-32-36"

class ChatBotRequest(APIView):
    #permission_classes = [IsAuthenticated]
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user: User = request.user

        msg = request.data['msg']

        response = openai.Completion.create(
            model=FINE_TUNED_MODEL,
            prompt=msg,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return Response(response["choices"][0]["text"].strip())