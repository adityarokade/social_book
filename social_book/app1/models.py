from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager
# Create your models here.





class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    user_name=models.CharField(max_length=80)
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    full_name=models.CharField(max_length=180)
    GENDER_CHOICES = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')

    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)

    CREDICT_CARD_TYPE_CHOICES = (
    ('option1','OPTION1'),
    ('option2', 'OPTION2'),
    ('option3', 'OPTION3'),
    )
    credict_card_type = models.CharField(max_length=7, choices=CREDICT_CARD_TYPE_CHOICES, default='option1')
    credict_card_number=models.IntegerField()
    cvc=models.CharField(max_length=100)
    expiration_date=models.CharField(max_length=12)

    public_visibility=models.BooleanField(default=True)
    birth_year=models.CharField(max_length=120)
    address=models.CharField(max_length=255)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['user_name','password1','password2','full_name','gender','city','state','credict_card_type','credict_card_number','cvc','expiration_date']
    
    objects = UserManager()



class UploadFiles(models.Model):
    email = models.EmailField(_("email address"), unique=True)

    file=models.FileField(upload_to='document/')
    
    title_of_book=models.CharField(max_length=255)
    Author_of_book=models.CharField(max_length=150)
    description=models.TextField(max_length=1000)
    visibility=models.BooleanField(default=True)
    cost_of_book=models.FloatField(max_length=10)
    Year=models.CharField(max_length=6)




    
    REQUIRED_FIELDS =['email','title_of_book','Author_of_book','description','visibility','cost_of_book','Year']

    
