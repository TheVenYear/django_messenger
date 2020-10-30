from django.urls import path
from rest_framework.routers import SimpleRouter

from chats.views import ChatsViewSet, MessagesView

router = SimpleRouter()
router.register('chats', ChatsViewSet, basename='chats')
router.register('messages', MessagesView, 'messages')


# urlpatterns = [
#     path('messages/', MessagesView.as_view(), name='messages')
# ]

urlpatterns = router.urls
