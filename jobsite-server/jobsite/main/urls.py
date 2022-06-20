from django.urls import include, path
from django.views.generic import TemplateView

from .user import api

urlpatterns = [
    path('', TemplateView.as_view(template_name="main.html")),
    path('register', api.Registration.as_view(), name='register'),
    path('login-google', api.LoginGoogle.as_view(), name='login-google'),
    path('test-auth', api.TestAuth.as_view(), name='test-auth'),
]