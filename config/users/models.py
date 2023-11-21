from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, last_name, first_name, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            username = username,
            email = email,
            first_name = first_name,
            last_name = last_name,
            is_active =  True,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, last_name, first_name, password, **extra_fields):
        user = self.create_user(username, email, last_name, first_name, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length = 30, unique = True)
    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    is_superuser = models.BooleanField(default=False)
    is_staff =  models.BooleanField(default=False)
    is_active =  models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def has_perm(self,perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        managed = False 
        db_table = 'auth_user'  