import json
from django.utils import timezone
from django.core import serializers

import traceback
import hashlib

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status

from main.employer.models import Employer

from ..utils import Utils

from .models import Job

from ..employer.authentication import EmployerJWTAuthentication


class Registration(APIView):
    authentication_classes = [EmployerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employer: Employer = request.user.employer

        job = Job()
        job.company = employer.company
        job.title = request.data['title']
        job.public_date = request.data['public_date']
        job.expired_date = request.data['expired_date']
        job.field = request.data['field']
        job.salary_min = request.data['salary_min']
        job.salary_max = request.data['salary_max']
        job.position = request.data['position']
        job.type = request.data['type']
        job.required_experience = request.data['required_experience']
        job.avaiable_slot = request.data['avaiable_slot']
        job.accepted_applicant = 0

        #if job.company != employer.company:
        #    return Response('job must belong to employer\'s company', status.HTTP_400_BAD_REQUEST)

        job.save()

        return Response(Utils.model_to_dict(job))

class Delete(APIView):
    authentication_classes = [EmployerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employer: Employer = request.user.employer

        job_id = request.data['id']
        jobs = Job.objects.filter(id=job_id)

        if jobs.exists() and jobs.first().company == employer.company:
            j: Job = jobs.first()
            j.delete()
            return Response('Done')
        else:
            return Response('Error', status.HTTP_400_BAD_REQUEST)

class Update(APIView):
    authentication_classes = [EmployerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employer: Employer = request.user.employer
        
        data = Utils.std_dict(request.data)
        job_id = data['id']
        jobs = Job.objects.filter(id=job_id)

        if jobs.exists() and jobs.first().company == employer.company:
            job: Job = jobs.first()
            job.title = request.data['title']
            job.public_date = request.data['title']
            job.expired_date = request.data['expired_date']
            job.field = request.data['field']
            job.salary_min = request.data['salary_min']
            job.salary_max = request.data['salary_max']
            job.position = request.data['position']
            job.type = request.data['type']
            job.required_experience = request.data['required_experience']
            job.avaiable_slot = request.data['avaiable_slot']
            job.accepted_applicant = request.data['accepted_applicant']
            job.save()
            return Response(Utils.model_to_dict(job))
        else:
            return Response('Error', status.HTTP_400_BAD_REQUEST)


class List(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(Utils.query_set_to_list(Job.objects.all()))


class Filter(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ret = []

        jobs = Job.objects.all()

        for job in jobs.iterator():
            dict_ = Utils.model_to_dict(job)
            for k, v in request.query_params.items():
                if type(v) == str and v.isdigit():
                    v = int(v)

                if dict_[k] == v:
                    ret.append(Utils.model_to_dict(job))
            
        return Response(ret)



class Detail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            job_id = request.data['id']
            job: Job = Job.objects.get(id=job_id)
            company = job.company

            job_dict = Utils.model_to_dict(job)
            job_dict['company'] = Utils.model_to_dict(company)

            return Response(job_dict)
        except:
            return Response('Error', status.HTTP_400_BAD_REQUEST)
