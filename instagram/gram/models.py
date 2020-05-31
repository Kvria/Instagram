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

