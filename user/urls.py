from django.urls import path
from user import views

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
]
