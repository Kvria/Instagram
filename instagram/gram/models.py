from django.contrib.auth.models import User
from django.db import models
# Create your models here



class Image(models.Model):
    image = models.ImageField(blank = True, null = True)
    image_id = models.IntegerField(primary_key = True)
    image_name = models.CharField(max_length = 50)
    image_caption = models.TextField(max_length = 500)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    # def __str__(self):
    #     return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length = 300)
    objects = models.Manager()

    def __str__(self):
        return f'{self.user} Profile'

    def save_profile(self):
        self.save()

    @classmethod
    def search_by_user(cls,search_term):
        users = User.objects.filter(username__icontains=search_term)
        return users

class Comment(models.Model):
    image = models.ForeignKey(Image, blank=True, on_delete=models.CASCADE, related_name='comment')
    commenter = models.ForeignKey(User, blank=True)
    comment = models.TextField()
    objects = models.Manager()

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_on_image(cls, id):
        the_comments = Comment.objects.filter(image__pk=id)
        return the_comments

    def __str__(self):
        return self.comment
    