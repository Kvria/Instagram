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

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)


        if u_form.is_valid():
            u_form.save()
            
            return render(request,'registration/profile.html')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
            'u_form': u_form

    }

    return render(request, 'registration/profile.html',locals())

def comment(request,image_id):
   current_user=request.user
   image = Image.objects.get(id=image_id)
   profile_user = User.objects.get(username=current_user)
   the_comments = Comment.objects.all()
   print(the_comments)
   if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
           comment = form.save(commit=False)
           comment.image = image
           comment.commenter = request.user

           commentf.save()

           print(the_comments)


       return redirect(instagram)

   else:
       form = CommentForm()

   return render(request, 'comment.html', locals())
