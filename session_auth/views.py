from django.contrib.auth import login, logout
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from django_messenger.utils import ApiRenderer
from session_auth.serializers import LoginSerializer, UserSerializer


@api_view(['GET'])
def me_view(request):
    return Response(UserSerializer(request.user).data)


@api_view(['DELETE'])
def logout_view(request):
    logout(request)
    return Response()


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(self.request, user)
        return Response(UserSerializer(serializer.validated_data).data)

