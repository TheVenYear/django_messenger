from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from chats.models import Chat
from chats.serializers import ChatRetrieveSerializer, ChatListSerializer, ChatEditSerializer


class ChatsViewSet(ModelViewSet):
    def create(self, request, **kwargs):
        super(ChatsViewSet, self).create(request, **kwargs)
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(members__in=[user])

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ChatRetrieveSerializer

        if self.action == 'list':
            return ChatListSerializer

        else:
            return ChatEditSerializer
