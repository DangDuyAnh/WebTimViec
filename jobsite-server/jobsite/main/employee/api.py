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

from .models import Employee, EmployeeAppliedJob, EmployeeSavedJob, EmployeeCv, EmployeeLetter
from ..user.model import User
from ..user.serializer import UserSerializer

from ..utils import Utils

from .authentication import EmployeeJWTAuthentication

from django.db import connection

import os
import sys
import pickle

import time
from django.conf import settings

import pandas as pd
import numpy as np

sys.path.append(os.path.join(settings.BASE_DIR, 'main/employee/recommender'))

from .recommender import job_recommender
from .recommender import latent_semantic_analysis
from .recommender.network_builder import *


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
        
        
class SelfProfile(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        _employee = request.user.employee
        employee = Utils.model_to_dict(_employee)
        user = UserSerializer(_employee.user, context={
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
        
        new = EmployeeSavedJob.objects.create(employee=employee, job=jobs.first())

        return Response(Utils.model_to_dict(new))


class SavedList(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee: Employee = request.user.employee
        items = EmployeeSavedJob.objects.filter(employee=employee)
        return Response(Utils.query_set_to_list(items))
        
        
class SavedRemove(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee: Employee = request.user.employee

        job_id = request.data['job_id']
        jobs = Job.objects.filter(id=job_id)
        
        if not jobs.exists():
            return Response('job_id doesn\'t exist', http_status.HTTP_400_BAD_REQUEST)

        items = EmployeeSavedJob.objects.filter(employee=employee, job=jobs.first())

        if not items.exists():
            return Response('employee didn\'t save job_id', http_status.HTTP_400_BAD_REQUEST)
            
        
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM employee_saved_job WHERE employee_id={employee.id} AND job_id={job_id}')
            
        #items.first().delete()

        return Response('Done')
        


class AddCV(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee: Employee = request.user.employee
        cv_id = int(request.data['cv_id'])

        cvs = EmployeeCv.objects.filter(employee=employee, cv_id=cv_id)

        if cvs.exists():
            return Response('cv exists', http_status.HTTP_400_BAD_REQUEST)

        newCV = EmployeeCv.objects.create(employee=employee, cv_id=cv_id)

        return Response(Utils.model_to_dict(newCV))


class RemoveCV(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee: Employee = request.user.employee
        cv_id = int(request.data['cv_id'])

        cvs = EmployeeCv.objects.filter(employee=employee, cv_id=cv_id)


        if cvs.exists():
            cv = cvs.first()
            with connection.cursor() as cursor:
                cursor.execute(f'DELETE FROM employee_cv WHERE employee_id={employee.id} AND cv_id={cv_id}')

            return Response('Done')
        else:
            return Response('cv doesn\'t exist', http_status.HTTP_400_BAD_REQUEST)


class ListCV(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee: Employee = request.user.employee
        cvs = EmployeeCv.objects.filter(employee=employee)
        return Response(Utils.query_set_to_list(cvs))


class SetMainCV(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee: Employee = request.user.employee
        cv_id = int(request.data['cv_id'])
        employee.main_cv_id = cv_id
        employee.save()
        return Response('Done')


class AddLetter(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee: Employee = request.user.employee
        letter_id = int(request.data['letter_id'])

        cvs = EmployeeLetter.objects.filter(employee=employee, letter_id=letter_id)

        if cvs.exists():
            return Response('letter exists', http_status.HTTP_400_BAD_REQUEST)

        newCV = EmployeeLetter.objects.create(employee=employee, letter_id=letter_id)
        
        return Response(Utils.model_to_dict(newCV))


class RemoveLetter(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee: Employee = request.user.employee
        letter_id = int(request.data['letter_id'])

        cvs = EmployeeLetter.objects.filter(employee=employee, letter_id=letter_id)

        if cvs.exists():
            cv = cvs.first()
            with connection.cursor() as cursor:
                cursor.execute(f'DELETE FROM employee_letter WHERE employee_id={employee.id} AND letter_id={letter_id}')
            return Response('Done')
        else:
            return Response('letter doesn\'t exist', http_status.HTTP_400_BAD_REQUEST)


class ListLetter(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee: Employee = request.user.employee
        cvs = EmployeeLetter.objects.filter(employee=employee)
        return Response(Utils.query_set_to_list(cvs))


class SetMainLetter(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee: Employee = request.user.employee
        letter_id = int(request.data['letter_id'])
        employee.main_letter_id = letter_id
        employee.save()
        return Response('Done')



def load_recommender():
    graphpath =  os.path.join(settings.BASE_DIR, 'main/employee/recommender/data/graph.pkl')
    lsapath = os.path.join(settings.BASE_DIR, 'main/employee/recommender/data/lsa.pkl')
    with open(graphpath, 'rb') as f:
        G = pickle.load(f)

    with open(lsapath, 'rb') as f:
        lsa = pickle.load(f)

    jrec = job_recommender.JobRecommender(G, lsa)

    return jrec

all_expertises = ['Java Developer', 'Testing', 'DevOps Engineer', 'Python Developer',
       'Web Designing', 'Hadoop', 'Blockchain', 'ETL Developer',
       'Operations Manager', 'Data Science', 'Mechanical Engineer',
        'Database', 
        'Business Analyst', 'DotNet Developer', 'Automation Testing',
       'Network Security Engineer', 'SAP Developer', 'Civil Engineer',
       ]
       

jrec = load_recommender()
user_data = {}

class JobRecommend(APIView):
    authentication_classes = [EmployeeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_data = {}
        user_data['expertise'] = request.data['expertise']
        user_data['resume'] = request.data['resume']
        if len(user_data['resume']) > 100:
            jrec.add_node_to_graph('candidate', user_data)

        num_recommend = int(request.data['n'])
        alpha = float(request.data['alpha'])
        personalized_results = jrec.rank_nodes(False, jrec.target_node, 'job', alpha)
        personalized_results = {key:item for i, (key,item) in enumerate(personalized_results.items()) if i < num_recommend}     
        
        ret = []
        for key, value in personalized_results.items():
            job_node = jrec.G.nodes[key]
            company_id = job_node['company_id']
            ret.append({
                'company_id'    : company_id,
                'job_name'      : job_node['job_name'],
                'taglist'       : job_node['taglist'],
                'location'      : job_node['location'],
                'description'   : job_node['description'],
                'logo_link'     : jrec.G.nodes[company_id]['logo_link'],
            })
            
        return Response(ret)