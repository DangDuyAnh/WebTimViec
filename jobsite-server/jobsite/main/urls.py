from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('', TemplateView.as_view(template_name="main.html")),
    path('user/', include('main.user.urls')),
    path('company/', include('main.company.urls')),
    path('job/', include('main.job.urls')),
    path('employer/', include('main.employer.urls')),
    path('employee/', include('main.employee.urls')),
    path('chat-room/', include('main.chat_room.urls')),
    path('province/list', api.ListProvince.as_view()),
]