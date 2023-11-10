from django.shortcuts import render
from django.http import HttpResponse
from .models import diary_collections

def index(request):
    return HttpResponse("<h1>App is running</h1>")

def add_diary(request):
    records = {
        "diaryID":"123",
        "userName":"kate"
    }
    diary_collections.insert_one(records)
    return HttpResponse("New diary is added")

def get_all_diary(request):
    diary = diary_collections.find()
    return (diary)