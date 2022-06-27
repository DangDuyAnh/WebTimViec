from django.urls import include, path
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    path('', TemplateView.as_view(template_name="main.html")),
    path('user/', include('main.user.urls')),
    path('company/', include('main.company.urls')),
    path('province/list', api.ListProvince.as_view()),
]