from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from chats.models import Chat
from chats.serializers import ChatRetrieveSerializer, ChatListSerializer, ChatEditSerializer


class ChatsViewSet(ModelViewSet):
    queryset = Chat.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ChatRetrieveSerializer

        if self.action == 'list':
            return ChatListSerializer

        else:
            return ChatEditSerializer
