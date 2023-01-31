"""social_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from django.views.generic import TemplateView

from app1 import views
# from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signup/',views.sign_up,name='signup'),
    # path('login/',views.user_login,name='login'),
    # path('profile/',views.user_profile,name='profile'),
    # path('authors_sellers/',views.Authors_and_sellers,name='authors_sellers'),
    path('upload_file/<email>/',views.upload_files,name='upload_file'),
    path('existing_files/<str:email>/<str:token>/',views.show_existing_files_to_user,name='existing_files'),
         
    # path(r'upload_file/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.upload_files,name='upload_files'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),



    path('register/',views.djoser_view1,name='register'),
    # path(r'^activate/<uid>/<token>/',views.get_token,name='okk'),
    # path(r'http://localhost:8000/activate/<uid>/<token>/', views.get_token, name='okk'),
    # path(r'activate/<uid>/<token>/$', views.get_token, name='urlname')
    # url(r'^users/(?P<uid>\d+)/(?P<token>\d+)$',views.get_token, name='urlname')
    # path('<uid>/<token>/',views.get_token),
    path('activate/<str:uid>/<str:token>', views.activate),
    # path('login_user/',views.login_user),
    path('',views.login_user,name="login_user"),
    path('user_list/<str:email>/<str:token>/',views.User_list,name='user_list'),
    path('dashbord/<str:email>/<str:token>/',views.dashbord,name='dashbord'),

    path('generate_token/',views.generate_token,name="generate_token"),
    path('specific_files/<str:token>/<str:email>/',views.access_specific_files_using_token,name="specific_files"),
    path('existing_files_warapper/<email>/',views.acess_files_wrapper1,name='existing_files_wrapper'),
    

         
]
# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]









