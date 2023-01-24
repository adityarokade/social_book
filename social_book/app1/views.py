from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,UploadFiles
from .forms import SignupFrom,UploadFilesForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
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
        print(fm.is_valid())
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

            return redirect('/result/{}/'.format(email))

        
    else:
        fm=UploadFilesForm()
        # print(fm)


    
    return render(request,'app1/upload_files.html',{'form':fm})

def show_existing_files_to_user(request,email):
    data=UploadFiles.objects.filter(email=email)

    return render(request,'app1/show_existing_files_to_user.html',{'data':data})

def user_profile(request):
    return render(request,'app1/profile.html')