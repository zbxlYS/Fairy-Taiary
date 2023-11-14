from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create_diary/", views.create_diary, name='create_diary'),

]