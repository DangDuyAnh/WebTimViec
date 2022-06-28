from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('create-pair', api.CreatePair.as_view(), name='create'),
    path('send', api.Send.as_view(), name='send'),
    path('conversation', api.Conversation.as_view(), name='conversation'),
    path('list', api.List.as_view(), name='list'),
    path('members-list', api.MembersList.as_view(), name='members-list'),
    path('members-detail-list', api.MembersDetailList.as_view(), name='members-detail-list'),
]