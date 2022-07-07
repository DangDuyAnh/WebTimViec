from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('profile', api.Profile.as_view(), name='profile'),
    path('apply', api.Apply.as_view(), name='apply'),
    path('save', api.Save.as_view(), name='save'),
    path('applied-list', api.AppliedList.as_view(), name='apply-l'),
    path('saved-list', api.SavedList.as_view(), name='save-l'),

    path('add-cv', api.AddCV.as_view(), name='add-cv'),
    path('remove-cv', api.RemoveCV.as_view(), name='remove-cv'),
    path('cv-list', api.ListCV.as_view(), name='cv-list'),

    path('add-letter-cv', api.AddCV.as_view(), name='add-letter-cv'),
    path('remove-letter-cv', api.RemoveCV.as_view(), name='remove-letter-cv'),
    path('cv-letter-list', api.ListLetterCV.as_view(), name='cv-letter-list'),
]