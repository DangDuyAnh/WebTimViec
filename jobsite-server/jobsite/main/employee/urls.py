from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('profile', api.Profile.as_view(), name='profile'),
    path('apply', api.Apply.as_view(), name='apply'),
    path('save', api.Save.as_view(), name='save'),
    path('applied-list', api.AppliedList.as_view(), name='apply-l'),
    path('saved-list', api.SavedList.as_view(), name='save-l'),
]