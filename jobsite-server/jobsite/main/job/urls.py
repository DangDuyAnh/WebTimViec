from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('register', api.Registration.as_view(), name='register'),
    path('delete', api.Delete.as_view(), name='delete'),
    path('update', api.Update.as_view(), name='update'),
    path('list', api.List.as_view(), name='list'),
    path('filter', api.Filter.as_view(), name='filter'),
    path('detail', api.Detail.as_view(), name='detail'),
]