import json
from django.utils import timezone
from django.core import serializers

import traceback
import hashlib

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status as http_status

from ..employee.models import EmployeeAppliedJob

from ..job.models import Job

from .models import Employer

from ..utils import Utils

from ..employer.authentication import EmployerJWTAuthentication


class GetCompany(APIView):
    authentication_classes = [EmployerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employer: Employer = request.user.employer
        return Response(Utils.model_to_dict(employer.company))


class JobList(APIView):
    authentication_classes = [EmployerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employer: Employer = request.user.employer

        return Response(Utils.query_set_to_list(Job.objects.filter(company_id=employer.company_id)))


class ApplicantList(APIView):
    authentication_classes = [EmployerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        applicants = None
        status = None

        employer: Employer = request.user.employer
        job_id = request.query_params['job_id']

        jobs = Job.objects.filter(id=job_id)

        if not jobs.exists():
            return Response('job_id not found', http_status.HTTP_400_BAD_REQUEST)

        job: Job = jobs.first()

        if job.company != employer.company:
            return Response('job and company must have same employer', http_status.HTTP_400_BAD_REQUEST)

        if 'status' in request.query_params:
            status = request.query_params['status']

        if status is None:
            applicants = EmployeeAppliedJob.objects.filter(job=job)
        else:
            applicants = EmployeeAppliedJob.objects.filter(job=job, status=status)

        return Response(Utils.query_set_to_list(applicants))


class SetStatus(APIView):
    authentication_classes = [EmployerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employer: Employer = request.user.employer

        employee_id = request.data['employee_id']
        job_id = request.data['job_id']
        status = request.data['status']

        applicants = EmployeeAppliedJob.objects.filter(employee_id=employee_id, job_id=job_id)

        if not applicants.exists():
            return Response('Not found', http_status.HTTP_400_BAD_REQUEST)

        applicant: EmployeeAppliedJob = applicants.first()
        job: Job = applicant.job

        if job.company != employer.company:
            return Response('job and company must have same employer', http_status.HTTP_400_BAD_REQUEST)

        applicant.status = status
        applicant.save()

        return Response('Done')