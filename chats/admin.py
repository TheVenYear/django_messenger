from django.contrib import admin

from chats.models import Message, Chat


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'text', 'date')


class MessageInlineAdmin(admin.TabularInline):
    model = Message
    fields = ('sender', 'text', 'date')
    readonly_fields = ('date',)
    extra = 0


class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    fields = ('name', 'members')
    inlines = (MessageInlineAdmin,)


admin.site.register(Chat, ChatAdmin)
