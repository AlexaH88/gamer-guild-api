from django.urls import path
from responses import views


urlpatterns = [
    path('responses/', views.ResponseList.as_view()),
    path('responses/<int:pk>/', views.ResponseDetail.as_view()),
]
