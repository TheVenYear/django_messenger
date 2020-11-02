from rest_framework import serializers

from chats.models import *
from session_auth.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Message
        exclude = ('chat',)


class MessageEditSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        chat = validated_data.get('chat')
        try:
            Chat.objects.get(id=chat.id, members__in=[user])
        except Chat.DoesNotExist:
            raise serializers.ValidationError('У вас нет доступа к этому чату')
        return Message.objects.create(sender=user, **validated_data)

    class Meta:
        model = Message
        fields = ('text', 'chat')


class ChatRetrieveSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    members = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = '__all__'


class ChatListSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = '__all__'


class ChatEditSerializer(serializers.ModelSerializer):
    def validate_members(self, attrs):
        user = self.context['user']
        if user not in attrs:
            attrs.append(user)

        return attrs

    class Meta:
        model = Chat
        exclude = ('date',)
