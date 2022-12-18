# from django.db import models
# from django.contrib.auth.models import User
#
# # Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=128)
#     text = models.TextField(blank=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now_add=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def __str__(self):
#         return self.title
#
# class Category(models.Model):
#     name = models.CharField(max_length=128)
#     description = models.TextField(blank=True)
#     posts = models.ManyToManyField(Post, blank=True, related_name='categories')
#
#     # posts = models.CharField(max_length=128)
#     # posts = models.ForeignKey(Post, on_delete=models.CASCADE, null=True) # issue with this
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = 'Categories'




from django.db import models  # <-- This is already in the file
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name