from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username=models.CharField(max_length=50)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    phone= models.CharField(max_length=25, null=True, blank=True, )
    birth_date= models.DateField(null=True, blank=True)
    profile_picture= models.ImageField(upload_to='profile_images', null=True, blank=True)