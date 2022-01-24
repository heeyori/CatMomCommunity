from distutils.command.upload import upload
from django.db import models
from miniapp.utlils import upload_image

class User(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    user_pw = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_nickname = models.CharField(max_length=50)
    user_bitrh = models.DateTimeField()
    date_joined = models.DateTimeField()

class Cat(models.Model):
    cat_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    neutral = models.CharField(max_length=10)
    location1 = models.CharField(max_length=50)
    location2 = models.CharField(max_length=50)
    location3 = models.CharField(max_length=50)
    appearance = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class Img(models.Model):
    objects = models.Manager()
    img = models.ImageField(upload_to=upload_image)