import json
from django.utils import timezone
from django.core import serializers

import traceback
import hashlib

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status as http_status

from main.job.models import Job

from .models import Employee, EmployeeAppliedJob, EmployeeSavedJob
from ..user.model import User
from ..user.serializer import UserSerializer

from ..utils import Utils

from .authentication import EmployeeJWTAuthentication


class Profile(APIView):
    #authentication_classes = [Sfa]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        id = request.query_params['id']
        employee_model = Employee.objects.get(id=id)
        employee = Utils.model_to_dict(employee_model)
        user = UserSerializer(employee_model.user, context={
                'request': request,
            }).data

        employee['user'] = user
        return Response(employee)


class Apply(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee: Employee = request.user.employee

        job_id = request.data['job_id']

        items = EmployeeAppliedJob.objects.filter(employee=employee)

        if items.exists():
            for i in items.iterator():
                #i: EmployeeAppliedJob
                if i.job.id == job_id:
                    return Response('Duplicate employee apply request', http_status.HTTP_400_BAD_REQUEST)


        jobs = Job.objects.filter(id=job_id)

        if not jobs.exists():
            return Response('job_id not found', http_status.HTTP_400_BAD_REQUEST)

        new = EmployeeAppliedJob.objects.create(employee=employee, job=jobs.first(), status=0)

        return Response(Utils.model_to_dict(new))


class AppliedList(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee: Employee = request.user.employee
        items = EmployeeAppliedJob.objects.filter(employee=employee)
        return Response(Utils.query_set_to_list(items))


class Save(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee: Employee = request.user.employee

        job_id = request.data['job_id']

        items = EmployeeSavedJob.objects.filter(employee=employee)

        if items.exists():
            for i in items.iterator():
                #i: EmployeeAppliedJob
                if i.job.id == job_id:
                    return Response('Duplicate employee save request', http_status.HTTP_400_BAD_REQUEST)


        jobs = Job.objects.filter(id=job_id)

        if not jobs.exists():
            return Response('job_id not found', http_status.HTTP_400_BAD_REQUEST)
        
        new = EmployeeSavedJob.objects.create(employee=employee, job=jobs.first(), status=0)

        return Response(Utils.model_to_dict(new))


class SavedList(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee: Employee = request.user.employee
        items = EmployeeSavedJob.objects.filter(employee=employee)
        return Response(Utils.query_set_to_list(items))