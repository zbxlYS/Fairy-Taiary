from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import diary_collections
from datetime import datetime

def index(request):
    return HttpResponse("<h1>App is running</h1>")

def get_all_diary(request):
    diaries = diary_collections.find()
    return render(request, 'diary_list.html', {'diaries': diaries})

'''
Diary 
'''

#Create
@login_required
def create_diary(request):
    print(request.user)
    if request.method == 'POST':
        user_id = request.user.id 
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        image_id = request.POST.get('image_id', '')
        date = datetime.now()
        new_diary={ 
            "user_id": user_id,
            "title": title,
            "content": content,
            "image_id": image_id,
            "date": date
        }
        diary_collections.insert_one(new_diary)
        
        return HttpResponse("Complete create diary")

    else:
        # GET 요청에 대한 폼 표시
        return render(request, 'create_diary.html') 

# Read Diary
def read_diary(request, diary_id):
    diary = diary_collections.find_one({'_id':diary_id})
    if diary: 
        return render(request, 'read_diary.html', {'diary': diary})
    else:
        return HttpResponse(f"User with ID {diary_id} does not exist.")

# Update Diary

# Delete Diary

'''
Diary 
'''

'''
Diary Collection CRUD+search
'''
# Create Diary

'''
def search_by_user(request, user):
    # 사용자(User)로 다이어리를 검색
    diaries = diary_collections.find({"user": user})
    return render(request, 'diary_list.html', {'diaries': diaries})

def search_by_date(request, date):
    # 날짜(Date)로 다이어리를 검색
    diaries = diary_collections.find({"date": date})
    return render(request, 'diary_list.html', {'diaries': diaries})

def search_by_image_id(request, image_id):
    # 이미지 ID(ImageID)로 다이어리를 검색
    diaries = diary_collections.find({"image_id": image_id})
    return render(request, 'diary_list.html', {'diaries': diaries})
'''