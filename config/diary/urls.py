from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add/',views.add_diary),
    path('show/',views.get_all_diary)
]