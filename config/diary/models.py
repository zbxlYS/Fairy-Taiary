from django.db import models
from db_connection import db

# Create your models here.

# we dont need models with mongoDB
# Diary 라는 이름의 collection 생성
diary_collections=db['Diary'] 
