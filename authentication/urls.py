from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path("logout/", views.custom_logout, name="logout"),
    path("password/reset/", views.reset_password, name="reset_password"),
]