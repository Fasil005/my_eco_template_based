from django.test import TestCase

from accounts.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(fullname="lion", username="roar")
        User.objects.create(fullname="cat", username="meow")
    
    def test_user(self):
        user = User.objects.all()
        print(user)