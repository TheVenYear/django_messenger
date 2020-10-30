from django.shortcuts import render
from rest_framework import status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from chats.models import Chat, Message
from chats.serializers import ChatRetrieveSerializer, ChatListSerializer, ChatEditSerializer, MessageEditSerializer, \
    MessageSerializer


class MessagesView(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    serializer_class = MessageEditSerializer

    def get_serializer_context(self):
        context = super(MessagesView, self).get_serializer_context()
        context.update({'request': self.request})
        return context

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user)


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
