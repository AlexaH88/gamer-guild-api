from django.urls import path
from socials import views


urlpatterns = [
    path('socials/', views.SocialList.as_view()),
    path('socials/<int:pk>/', views.SocialDetail.as_view()),
]
