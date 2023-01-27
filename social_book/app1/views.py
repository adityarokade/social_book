from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,UploadFiles
from .forms import SignupFrom,UploadFilesForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
import requests
import json










# Create your views here.
def sign_up(request):
    if request.method=="POST":
        fm =SignupFrom(request.POST)
        # print(fm.is_valid())
        # print(fm.errors)
        if fm.is_valid():
            print("Fm is valid")
            # print("--**__"*20)
            # email=fm.cleaned_data['email']
            # user_name= fm.cleaned_data['user_name']

            # # messages.success(request,'Account created successufully')
            # print(email)
            # print(user_name)

            fm.save()
            print("Form is saved")
    else:
        fm=SignupFrom()
        
        
    return render (request,'app1/register.html',{'form':fm})


def user_login(request):
    if request.method == "POST":
        print("started")
        fm=AuthenticationForm(request=request,data=request.POST)
        
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            print(uname,upass)
            
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm()
    return render(request,'app1/login.html',{'form':fm})

def Authors_and_sellers(request):

    try:
        data=CustomUser.objects.all()
        print(data)

    except:
        print("Error in authors and sellers ")


    return render(request,'app1/authors_sellers.html',{'data':data})

def upload_files(request,email):
    if request.method=="POST":
        fm=UploadFilesForm(request.POST ,request.FILES)
        
        print(fm.is_valid())
        print(fm.errors)
        if fm.is_valid():

            messages.success(request,'File Uploaded Successufully')
            # fm.changed_data
            print(email)
            file_input=fm.cleaned_data['file']
            print(file_input)
            # fm.email=email1
            
            fm.save()

            return HttpResponseRedirect('/existing_files/{}/'.format(email))

        
    else:
        fm=UploadFilesForm()
        # print(fm)


    
    return render(request,'app1/upload_files.html',{'form':fm})

def show_existing_files_to_user(request,email):
    
    data=UploadFiles.objects.filter(email=email)
    if data is not None:
        return render(request,'app1/show_existing_files_to_user.html',{'data':data})
    else:
        return HttpResponseRedirect('/upload_file/{}/'.format(email))


def user_profile(request):
    return render(request,'app1/profile.html')

def djoser_view1(request):  # generate token and create user
    


    if request.method=="POST":

        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1!=password2:
            return HttpResponse("<h3 style='color:red'>The password and Confirm password not same</h3>")
        

        URL = "http://localhost:8000/auth/users/"

        payload = json.dumps({
                        "email": email,
                        'first_name':first_name,
                        'last_name':last_name,
                        "password": password1,
                        "re_password": password2
                    })
        headers = {
                         'Content-Type': 'application/json'
                    }

        response = requests.request("POST", URL, headers=headers, data=payload)

        

        return HttpResponse(f"<h2> Account Creditaced Response:- {response.text} </h2>")

    else:
        return render(request,'app1/create_token.html')
    



base_url="http://localhost:8000/"
def activate(request, uid, token):
    endpoint = base_url + "auth/users/activation/"
    r = requests.post(endpoint, json={"uid":uid,"token":token})

    # return redirect('upload_file/{}/'.format(email))

    # print(r)
    # return HttpResponse(f"<h3> token access sus. url-{r} &&&& {uid} & {token}</h3>")
    return HttpResponseRedirect('/login_user/')



def login_user(request):
    if request.method=="POST":

        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            # return redirect('existing_files/{}/'.format(username))
            return HttpResponseRedirect('/existing_files/{}/'.format(username))
        else:
            return HttpResponse(f"<h2>Please provide the correct {username} Username and {password}Password </h2>")
    else:
        return render(request,'app1/login_djoser.html')






def user_me(request):
    endpoint = base_url + "auth/users/me/"
    r= requests.get(endpoint)
    print(r)
    return HttpResponse(f"<h3>user--{r},{ r.USERNAME_FIELD }</h3>")











































from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.parsers import JSONParser
import io
from .serializers import UserCreateSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['POST'])
def student_create(request):
    if request.method == 'POST':
       serializer = UserCreateSerializer(data = request.data)
       if serializer.is_valid():
           serializer.save()
           res = {'msg': 'Data Created'}
           return Response(res, status=status.HTTP_201_CREATED)
       return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = UserCreateSerializer()
    return 

   