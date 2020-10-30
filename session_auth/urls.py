from django.urls import path
from rest_framework import routers

from session_auth.views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('me/', me_view, name='me'),
]
