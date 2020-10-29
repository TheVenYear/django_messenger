from django.contrib.auth import login
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from session_auth.serializers import LoginSerializer, UserSerializer


@api_view(['GET'])
def me(request):
    return Response('YOU')


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(self.request, user)
        return Response(UserSerializer(serializer.validated_data).data)


@api_view(['DELETE'])
def logout(request):
    return Response('LOGOUT')
