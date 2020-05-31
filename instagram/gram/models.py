from django.db import models

# Create your models here
class Category(models.Model):
    category_name = models.CharField(max_length = 45)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category_name

    @classmethod
    def update_category(id,value):
        Category.objects.filter(id = id).update(name = value)\
    
    @classmethod
    def display_all_categories(cls):
        return cls.objects.all()

class Location(models.Model):
    location_name = models.CharField(max_length = 30)
    objects = models.Manager()

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(id,value):
        Location.objects.filter(id = id).update(name = value)

    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()

class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    user_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class Image(models.Model):
    photos = models.ImageField(upload_to= 'images/')
    image_id = models.IntegerField(primary_key = True)
    image_name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 100)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def display_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        images = cls.objects.get(id = id)
        return images

    @classmethod
    def filter_by_location(cls,location_term):
        locations = cls.objects.filter(location__i_location__icontains=location_term)
        return locations

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__i_category__icontains=search_term)
        return images