from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('register', api.Registration.as_view(), name='register'),
    path('list', api.List.as_view(), name='list'),
]