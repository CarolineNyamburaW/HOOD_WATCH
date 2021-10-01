from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = CloudinaryField('image', default = '.jpg,.png')

  def __str__(self):
    return f'{self.user.username} Profile'

class Hood(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)
  def __str__(self):
      return self.name

class Photo(models.Model):
  hood = models.ForeignKey( Hood, on_delete=models.SET_NULL, null=True, blank=True )
  image = CloudinaryField('image', default = '.jpg,.png')
  description= models.TextField()

  def __str__(self):
      return self.description