from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('register', api.Registration.as_view(), name='register'),
    path('login-google', api.LoginGoogle.as_view(), name='login-google'),
    path('test-auth', api.TestAuth.as_view(), name='test-auth'),

    path('set-role', api.SetRole.as_view(), name='set-role'),
]