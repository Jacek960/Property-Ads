from django.contrib.auth import user_logged_in
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name= models.CharField(max_length=120)
    phone_number = models.CharField(max_length=12)
    profile_image = models.ImageField(default='profile_pic.jpg', upload_to = 'profile_pic')
    first_name= models.CharField(max_length=120,blank=True)
    last_name= models.CharField(max_length=120, blank=True)
    email= models.EmailField(max_length=254,blank=True)

    def __str__(self):
        return self.user


def create_profile(sender, user, request, **kwargs):
    Profile.objects.get_or_create(user=user)

user_logged_in.connect(create_profile)
