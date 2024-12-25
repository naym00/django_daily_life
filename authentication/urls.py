from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
]