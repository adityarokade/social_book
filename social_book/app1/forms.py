from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser,UploadFiles
from django.core import validators

class SignupFrom(UserCreationForm):
    
    class Meta:
        model=CustomUser
        # fields=['email','user_name','password1','password2','full_name','gender','city','state','credict_card_type','credict_card_number','cvc','expiration_date','public_visibility','birth_year','address']
        fields=['email','first_name','last_name']
        
        labels={'email':"Email"}

class UploadFilesForm(forms.ModelForm):
    class Meta:
        model=UploadFiles
        fields=['email','file','title_of_book','Author_of_book','description','visibility','cost_of_book','Year']
        labels={'email':'Email','file':'File','title_of_book':'Title','Author_of_book':'Author'}



