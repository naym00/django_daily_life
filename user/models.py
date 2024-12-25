from django.db import models
from django.contrib.auth.models import AbstractUser
from help.choice import choice as CH
from help.common.a import A as HELP

def upload_profile_pic(instance, filename):
    if filename[-4:] == '.jpg':
        return "files/user/{username}/profile_pic/{unique}.jpg".format(username=instance.user.username, unique=HELP().uniqueNumber())

def upload_cover_photo(instance, filename):
    if filename[-4:] == '.jpg':
        return "files/user/{username}/cover_photo/{unique}.jpg".format(username=instance.user.username, unique=HELP().uniqueNumber())

class User(AbstractUser):
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=HELP().listToTuple(CH.GENDER))

    def __str__(self):
        return f'{self.username} - {self.is_superuser}'

class Profilepic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profilepic_user')
    image = models.ImageField(upload_to=upload_profile_pic, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.is_active}'

class Coverphoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coverphoto_user')
    image = models.ImageField(upload_to=upload_cover_photo, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.is_active}'