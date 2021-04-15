from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Problem(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title

