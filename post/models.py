from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)  # auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)  # auto_now=True will automatically update the field whenever the object is saved.