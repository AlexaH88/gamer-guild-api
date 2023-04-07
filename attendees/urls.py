from django.urls import path
from attendees import views


urlpatterns = [
    path('attendees/', views.AttendeeList.as_view()),
    path('attendees/<int:pk>/', views.AttendeeDetail.as_view()),
]
