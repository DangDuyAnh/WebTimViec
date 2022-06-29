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

from .models import Company

class Registration(APIView):
    #permission_classes = [IsAuthenticated]
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        name = request.data['name']

        if Company.objects.filter(name=name).exists():
            return Response('Company exists', status.HTTP_400_BAD_REQUEST)

        company = Company()
        company.name = request.data['name']
        company.address = request.data['address']
        company.province_id = request.data['province_id']
        company.desc = request.data['desc']
        company.status = 1
        company.save()
        
        return Response(Utils.model_to_dict(company))


class List(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all = Company.objects.filter(status=1)
        arr = []
        for p in all.iterator():
            arr.append(Utils.model_to_dict(p))

        return Response(arr)