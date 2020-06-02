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
