from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *
from .form import *

# Create your views here.
@login_required(login_url = "accounts/login")
def index(request):
    images=Image.objects.all()
    return render(request,'index.html',{"images":images})

def welcome(request):
    if request.user.is_authenticated():
        return redirect('index')
    else:
        form = SignupForm()
    return render(request,'registration/login.html', {"form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    pics = Image.objects.all()
    profile = Profile.objects.all()
