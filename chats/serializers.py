from rest_framework import serializers

from chats.models import *
from session_auth.serializers import UserSerializer


class MessageListSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Message
        exclude = ('chat',)


class ChatRetrieveSerializer(serializers.ModelSerializer):
    messages = MessageListSerializer(many=True)
    members = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = '__all__'


class ChatListSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'name', 'members')


class ChatEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        exclude = ('date',)