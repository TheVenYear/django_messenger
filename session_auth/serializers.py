from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        read_only_fields = ('id', 'username', 'email')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Неверный логин или пароль')
        if not user.is_active:
            raise serializers.ValidationError('Пользователь не активен')

        return user

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
