from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('ask', api.ChatBotRequest.as_view(), name='ask'),
]