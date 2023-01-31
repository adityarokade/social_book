from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect


from app1.models import UploadFiles

def upload_test_function(email):
    data=UploadFiles.objects.filter(email=email)
    print(data)
    if data:
        return True
    return False

def upload_required():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            print(request.user)
            a=upload_test_function(request.user)
            print(a)
            if a==False:
                print(a,"flase")
                return HttpResponseRedirect('/upload_file/{}/'.format(request.user))
            else:
                return view(request, *args, **kwargs)
        return _wrapped_view
    return decorator