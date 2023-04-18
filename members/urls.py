from django.urls import path
from members import views


urlpatterns = [
    path('members/', views.MemberList.as_view()),
    path('members/<int:pk>/', views.MemberDetail.as_view()),
]
