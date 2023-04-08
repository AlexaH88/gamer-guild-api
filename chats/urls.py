from django.urls import path
from chats import views


urlpatterns = [
    path('chats/', views.ChatList.as_view()),
]
