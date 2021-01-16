import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'
        
    name = models.CharField(max_length=20)

    # Function to show category name
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    # Function to return text of post title
    def __str__(self):
        return self.title

   

    # Function to return post created 1 day ago
    def was_created_recently(self):
        return self.created_on >= timezone.now() - datetime.timedelta(days=1)

    # Function to return any posts modified in the last day
    def was_modified_recently(self):
        return self.last_modified >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author

    

    