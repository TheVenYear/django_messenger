from django.urls import path

from session_auth.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('me/', me, name='me'),
]
