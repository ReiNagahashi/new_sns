from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.
def upload_to(instance,filename):
    return 'problems/{filename}'.format(filename=filename)

options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

class Problem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    thumb = models.ImageField(_("Image"),upload_to=upload_to,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date',)
    def __str__(self):
        return self.title 