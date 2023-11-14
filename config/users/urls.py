from django.urls import path

from . import views


urlpatterns = [
    
    path('create_user/', views.create_user, name='create_user'),
    path('read_user/<str:user_id>/', views.read_user, name='read_user'),
    path('update_user/<str:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<str:user_id>/', views.delete_user, name='delete_user'),
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
]