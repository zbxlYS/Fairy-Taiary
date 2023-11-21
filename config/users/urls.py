from django.urls import path
from .views import register_view, update_user_view
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/', update_user_view, name='update_user'),
]