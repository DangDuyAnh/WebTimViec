from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('company', api.GetCompany.as_view(), name='company'),
    path('job-list', api.JobList.as_view(), name='job-list'),
    path('applicant-list', api.ApplicantList.as_view(), name='applicant-list'),
    path('set-status', api.SetStatus.as_view(), name='set-status'),
]