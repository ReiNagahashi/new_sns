from django.db import models
from django.db.models import constraints
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


def upload_to(instance,filename):
    return 'profile/{filename}'.format(filename=filename)

class CustomAccountManager(BaseUserManager):
    def create_user(self,email,password,**other_fields):
        if not email:
            raise ValueError(_('メールアドレスを入力してください'))
        email = self.normalize_email(email)
        user = self.model(email=email,**other_fields)
        user.set_password(password)
        user.save()

        return user
    def create_superuser(self,email,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if not email:
            raise ValueError(_('メールアドレスを入力してください'))

        return self.create_user(email,password,**other_fields)

# Customise the user model
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True)
    fullname = models.CharField(max_length=100)
    introduction = models.TextField(null=True,max_length=70)
    date = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(_("Image"),upload_to=upload_to,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()    

    USERNAME_FIELD='email'

# follow user
class UserFollowing(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="following")
    following_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="followers")
    timestamp = models.DateTimeField(auto_now_add=True)