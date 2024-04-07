from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CategoryModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='blogs')

def __str__(self):
    return self.title

class Meta:
    verbose_name = 'blog'
    verbose_name_plural = 'blogs'
    ordering = 'id',




