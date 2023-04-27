from django.urls import path
from discussions import views


urlpatterns = [
    path('discussions/', views.DiscussionList.as_view()),
    path('discussions/<int:pk>/', views.DiscussionDetail.as_view()),
]
