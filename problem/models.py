from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Problem(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    thumb = models.ImageField(null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return self.title