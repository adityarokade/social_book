from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
# from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager
# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     def get_full_name(self):
#         return self.first_name

#     def get_short_name(self):
#         return self.first_name
    
#     def __str__(self):
#         return self.email
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    # user_name=models.CharField(max_length=80)
    # password1=models.CharField(max_length=50)
    # password2=models.CharField(max_length=50)
    # full_name=models.CharField(max_length=180)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # GENDER_CHOICES = (
    # ('male','MALE'),
    # ('female', 'FEMALE'),
    # )
    # gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    gender=models.CharField(max_length=50)
    

    # city=models.CharField(max_length=150)
    # state=models.CharField(max_length=150)

    # CREDICT_CARD_TYPE_CHOICES = (
    # ('option1','OPTION1'),
    # ('option2', 'OPTION2'),
    # ('option3', 'OPTION3'),
    # )
    # credict_card_type = models.CharField(max_length=7, choices=CREDICT_CARD_TYPE_CHOICES, default='option1')
    # credict_card_number=models.IntegerField()
    # cvc=models.CharField(max_length=100)
    # expiration_date=models.CharField(max_length=12)

    public_visibility=models.BooleanField(default=True)
    # birth_year=models.CharField(max_length=120)
    # address=models.CharField(max_length=255)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['user_name','password1','password2','full_name','gender','city','state','credict_card_type','credict_card_number','cvc','expiration_date']
    REQUIRED_FIELDS = ['first_name','last_name']
    
    # objects = UserManager()
    # objects = UserAccountManager()
    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email



class UploadFiles(models.Model):
    email = models.EmailField(max_length=255)

    file=models.FileField(upload_to='document/',unique=True)
    
    title_of_book=models.CharField(max_length=255)
    Author_of_book=models.CharField(max_length=150)
    description=models.TextField(max_length=1000)
    visibility=models.BooleanField(default=True)
    cost_of_book=models.FloatField(max_length=10)
    Year=models.CharField(max_length=6)




    
    REQUIRED_FIELDS =['email','title_of_book','Author_of_book','description','visibility','cost_of_book','Year']

    


