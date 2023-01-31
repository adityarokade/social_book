from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,UploadFiles
from .forms import SignupFrom
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
import requests
import json
from django.core.mail import send_mail
from .email_notification import Notification


from .decorators import upload_required








base_url="http://localhost:8000/"



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
        
        
    return render (request,'app1/register1.html',{'form':fm})


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
        # fm=UploadFilesForm(request.POST ,request.FILES)
        
        # print(fm.is_valid())
        # print(fm.errors)
        # if fm.is_valid():
        File=request.POST['input_file']
        title_of_book=request.POST['title_of_book']
        Author_of_book=request.POST['Author_of_book']
        description=request.POST['description']
        visibility=request.POST['visibility']
        cost_of_book=request.POST['cost_of_book']
        Year=request.POST['Year']

            # messages.success(request,'File Uploaded Successufully')
            # fm.changed_data
            # print(email)
            # file_input=fm.cleaned_data['file']
            # print(file_input)
            # fm.email=email1
        print(File)
    
        try:
            up=UploadFiles(email=email,file=File,title_of_book=title_of_book,Author_of_book=Author_of_book,description=description,visibility=visibility,cost_of_book=cost_of_book,Year=Year)
            up.save()

            
        
        
            notification=Notification()
            subject="About File Upload in djangoapp"
            message=f"Hello, UserName:- {email} . File :-{File} is succefully uploaded."
            notification.Email_notification(subject,message,email)

            return HttpResponseRedirect('/dashbord/{}/'.format(email))
        except:
            HttpResponse("<h3>Some Error is Occured during file upload ,please check the file format (only pdf,jpg accepted)</h3>")

        
    # else:
        # fm=UploadFilesForm()
        # print(fm)


    
    return render(request,'app1/upload_files.html',{'email':email})


@upload_required()
def show_existing_files_to_user(request,email):
    
    data=UploadFiles.objects.filter(email=email)
    return render(request,'app1/show_existing_files_to_user.html',{'data':data,'email':email})

    # print(data)

    # if data :

    #     return render(request,'app1/show_existing_files_to_user.html',{'data':data,'email':email})
    # else:
    #     return HttpResponseRedirect('/upload_file/{}/'.format(email))


def user_profile(request):
    
    return render(request,'app1/profile.html')

def djoser_view1(request):  # generate token and create user
    


    if request.method=="POST":

        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gender=request.POST['gender']
        public_visibility=request.POST['public_visibility']
        password1=request.POST['password1']
        password2=request.POST['password2']

        # print(email)
        # print(first_name)
        # print(last_name)
        # print(gender)
        # print(public_visibility)
        # print(password1,password2)


        
        if password1!=password2:
            return HttpResponse("<h3 style='color:red'>The password and Confirm password not same</h3>")
        

        URL = "http://localhost:8000/auth/users/"

        payload = json.dumps({
                        "email": email,
                        'first_name':first_name,
                        'last_name':last_name,
                        "password": password1,
                        "re_password": password2,
                        "gender":gender,
                        "public_visibility":public_visibility
                    })
        headers = {
                         'Content-Type': 'application/json'
                    }

        response = requests.request("POST", URL, headers=headers, data=payload)

        

        return HttpResponse(f"<h2> Account Creditaced Response:- {response.text} |   Please Check the Your Register Mail</h2>")

    else:
        return render(request,'app1/register2.html')
    




def activate(request, uid, token):
    endpoint = base_url + "auth/users/activation/"
    r = requests.post(endpoint, json={"uid":uid,"token":token})
    

    # return redirect('upload_file/{}/'.format(email))

    # print(r)
    # return HttpResponse(f"<h3> token access sus. url-{r} &&&& {uid} & {token}</h3>")
    return HttpResponseRedirect('/')



def login_user(request):
    if request.method=="POST":

        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        # endpoint = base_url + "auth/jwt/create/"
        # r = requests.post(endpoint, json={"email":username,"password":password})
        
        # token=r.text.split(',')[1].split(':')[1]
      
        
    

        if user is not None:
            login(request,user)
            notification=Notification()
            subject="About Login in djangoapp"
            message=f"Hello, UserName:- {username} is succefully login"
            notification.Email_notification(subject,message,username)
            # return redirect('existing_files/{}/'.format(username))
            # return HttpResponseRedirect('/existing_files/{}/'.format(username))
            return HttpResponseRedirect('/dashbord/{}/'.format(username))
        else:
            return HttpResponse(f"<h2>Please provide the correctUsername and Password or check the token validity</h2>")
    else:
        return render(request,'app1/login_djoser.html')






def User_list(request,email):

    data=CustomUser.objects.all()
        
    return render(request,'app1/user_list.html',{'data':data,'email':email})


def dashbord(request,email):

    return render(request,'app1/dashbord.html',{'email':email})

def generate_token(request):
    if request.method=="POST":

        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        
        if user is not None:
            endpoint = base_url + "auth/jwt/create/"
            r = requests.post(endpoint, json={"email":username,"password":password})
        
            token=r.text.split(',')[1].split(':')[1]
            
            return HttpResponseRedirect('/specific_files/{}/{}/'.format(token,username))
        else:
            return HttpResponse(f"<h2>Please provide the correctUsername and Password or check the token validity</h2>")
    else:
        return render(request,'app1/login_djoser.html')






def access_specific_files_using_token(request,token,email):
    endpoint = base_url + "auth/jwt/verify/"
    r = requests.post(endpoint, json={"token":token})

    data=UploadFiles.objects.filter(email=email)
    print(data)

    if data :

        return render(request,'app1/show_existing_files_to_user.html',{'data':data,'email':email})
    else:
        return HttpResponseRedirect('/upload_file/{}/'.format(email))





@upload_required()
def acess_files_wrapper1(request,email):
    
    data=UploadFiles.objects.filter(email=email)

    return render(request,'app1/show_existing_files_to_user.html',{'data':data,'email':email})



























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

   