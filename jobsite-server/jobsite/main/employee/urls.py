from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('profile', api.Profile.as_view(), name='profile'),
    path('self-profile', api.SelfProfile.as_view(), name='self-profile'),
    path('apply', api.Apply.as_view(), name='apply'),
    path('save', api.Save.as_view(), name='save'),
    path('applied-list', api.AppliedList.as_view(), name='apply-l'),
    path('saved-list', api.SavedList.as_view(), name='save-l'),
    path('saved-remove', api.SavedRemove.as_view(), name='save-r'),

    path('add-cv', api.AddCV.as_view(), name='add-cv'),
    path('remove-cv', api.RemoveCV.as_view(), name='remove-cv'),
    path('cv-list', api.ListCV.as_view(), name='cv-list'),
    path('set-main-cv', api.SetMainCV.as_view(), name='set-main-cv'),

    path('add-letter', api.AddLetter.as_view(), name='add-letter'),
    path('remove-letter', api.RemoveLetter.as_view(), name='remove-letter'),
    path('set-main-letter', api.SetMainLetter.as_view(), name='set-main-letter'),
    path('letter-list', api.ListLetter.as_view(), name='letter-list'),

    path('job-recommend', api.JobRecommend.as_view(), name='job-recommend'),
    path('job-search', api.JobSearch.as_view(), name='job-search'),
]