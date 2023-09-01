from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Author(models.Model):
  added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return self.added_by

class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField(max_length=300 , null=True)  
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
