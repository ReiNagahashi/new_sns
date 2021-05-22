from django.db import models
from accounts.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.
def upload_to(instance,filename):
    return 'problems/{filename}'.format(filename=filename)

class ProblemLike(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    problem=models.ForeignKey('Problem',on_delete=models.CASCADE)

class Problem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    thumb = models.ImageField(_("Image"),upload_to=upload_to,null=True)
    video = models.FileField(upload_to='video/%y', blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name="problemLikes",blank=True)
    date = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-date',)
    def __str__(self):
        return self.title 
