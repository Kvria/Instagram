from django.db import models

# Create your models here

class Image(models.Model):
    image = models.ImageField(blank = True, null = True)
    image_name = models.Charfield(max_length = 50)
    image_caption = models.TextField
    profile = models.ForeignKey('User', on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=Timezone.now)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def search_by_user(cls,search_term):
        users = cls.objects.filter(title__icontains=search_term)
        return users

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()
