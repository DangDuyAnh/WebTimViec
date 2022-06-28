import json
from django.utils import timezone
from django.core import serializers

import traceback
import hashlib

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status

from .utils import Utils

from .models import Province
#from .serializer import ProvinceSerializer

class ListProvince(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        provinces = Province.objects.all()
        arr = []
        for p in provinces.iterator():
            arr.append(Utils.model_to_dict(p))

        return Response(arr)