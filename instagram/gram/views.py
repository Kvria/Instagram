from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment,User
from .forms import UserUpdateForm, ProfileUpdateForm, CommentsForm, Uploads
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse

# Create your views here.
@login_required(login_url = "accounts/login")
def home(request):
    images = Image.objects.all()
    return render(request,'index.html',{"images":images})


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

    context = {'u_form': u_form}

    return render(request, 'registration/profile.html',locals())

def comment(request,image_id):
   current_user=request.user
   image = Image.objects.get(id=id)
   profile_user = User.objects.get(username=current_user)
   the_comments = Comment.objects.all()
   print(the_comments)
   if request.method == 'POST':
       form = CommentsForm(request.POST)
       if form.is_valid():
           comment = form.save(commit=False)
           comment.image = image
           comment.commenter = request.user

           comment.save()

           print(the_comments)
       return redirect('home')
   else:
       form = CommentsForm()
   return render(request, 'comments.html', locals())

def search_users(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_users = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, '/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def post_new(request):
    current_user = request.user
    if request.method == 'POST':
        form = Uploads(request.POST, request.FILES)
        if form.is_valid():
            user_img = form.save(commit=False)
            user_img.profile = current_user
            user_img.save()
        return redirect('home')
    else:
        form = Uploads()
    return render(request, "new_post.html", {"form": form})

# def like(request, id):
#     post = Image.objects.get(id = id)
#     post.likes += 1
#     post.save()
#     return HttpResponseRedirect(reverse("index"))