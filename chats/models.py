from django.contrib.auth.models import User
from django.db.models import *

DELETED_USER = 1


class Chat(Model):
    name = CharField(max_length=300, verbose_name='название')
    members = ManyToManyField(User, related_name='chats', verbose_name='участники')
    date = DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'


class Message(Model):
    sender = ForeignKey(User, related_name='messages', on_delete=SET_NULL,
                        verbose_name='отправитель', null=True)
    text = CharField(max_length=3000, verbose_name='текст')
    chat = ForeignKey(Chat, related_name='messages', on_delete=CASCADE, verbose_name='чат')
    date = DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
