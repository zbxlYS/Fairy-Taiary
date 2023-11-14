from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from .models import users_collections
from datetime import datetime
# Create your views here.
'''
User CRUD
'''
#Create
def create_user(request):
    if request.method =='POST':
        user_id = request.POST.get('user_id','')
        email = request.POST.get('email','')
        existing_userid = users_collections.find_one({'user_id': user_id})
        existing_email = users_collections.find_one({'email': email})
        if existing_userid:
            return HttpResponse("User with the same user_id already exists.")
        if existing_email:
            return HttpResponse("User with the same email already exists.")
        
        name = request.POST.get('username','')
        password = request.POST.get('password','')
        hashed_password = make_password(password)
        date = datetime.now()
        
        new_user={ 
            'user_id':user_id,
            'name' : name,
            'email' : email,
            'password' : hashed_password,
            'date' : date,
        }
        users_collections.insert_one(new_user)
        
        return HttpResponse("Complete create users")
    else: 
        return render(request,'create_user.html')

#Read
def read_user(request, user_id):
    user = users_collections.find_one({'user_id':user_id})
    if user: 
        return render(request, 'read_user.html', {'user': user})
    else:
        return HttpResponse(f"User with ID {user_id} does not exist.")
    
#Update
def update_user(request, user_id):
    user = users_collections.find_one({'user_id':user_id})

    if user:
        if request.method == 'POST':
            # Update the user's name
            new_name = request.POST.get('name', '')
            users_collections.update_one({'user_id': user_id}, {'$set': {'name': new_name}})
            return HttpResponse(f"User {user_id} updated successfully!")

        else:
            # GET request, show the user update form
            return render(request, 'update_user.html', {'user': user})
    else:
        # User with the given _id doesn't exist
        return HttpResponse(f"User with ID {user_id} does not exist.")
    
#Delete
def delete_user(request, user_id):
    user = users_collections.find_one({'user_id':user_id})
    
    if user:
        if request.method == 'POST':
            users_collections.delete_one({'user_id': user_id})
            return render(request, 'delete_user.html', {'user': user})
    else:
        # GET request, show the user deletion confirmation page
        return HttpResponse(f"User with ID {user_id} does not exist.")
    
'''
LOG IN / OUT
'''
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id', '')
        password = request.POST.get('password', '')

        user = users_collections.find_one({'user_id': user_id})

        if user and check_password(password, user['password']):
            request.session['user_id'] = user['user_id']
            return HttpResponse(f"User {user_id} logged in successfully!")
        else:
            return HttpResponse("Invalid credentials. Please try again.")
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return HttpResponse("/")