
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Image,Profile,Comment,User

class SignupForm(UserCreationForm):
   email = forms.EmailField(max_length=200, help_text = 'Required')
   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_pic','bio']

class CommentsForm(forms.ModelForm):
    class Meta:
       model = Comment
       exclude = ['image','commenter']

class Uploads(forms.ModelForm):
    class Meta:
        model=Image
        exclude = ['profile','post_date']
        
        