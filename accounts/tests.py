from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserFollowing

# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(id=1,email="example@abc.com",password="something")
        self.userb = User.objects.create_user(id=2,email="exampleSecond@abc.com",password="something123")
    
    def test_user_created_via_signal(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(),2)
    
    def test_following(self):
        first = self.user
        second = self.userb
        UserFollowing.objects.create(user_id=first.id,following_user_id=second.id)
        