from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=256,blank=True)
    name = models.CharField(max_length=256,blank=True)
    address = models.CharField(max_length=256,blank=True)
    allName = models.CharField(max_length=256,blank=True)
    mobile = models.CharField(max_length=256,blank=True)
    logo = models.URLField(max_length=256,blank=True)
    city = models.CharField(max_length=256,blank=True)
    class Meta:
        unique_together=("user","city")

    def __str__(self):
        return str(self.name+self.username)

class Materials(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=256,blank=True)
    name = models.CharField(max_length=256,blank=True)
    address = models.CharField(max_length=256,blank=True)
    allName = models.CharField(max_length=256,blank=True)
    mobile = models.CharField(max_length=256,blank=True)
    logo = models.URLField(max_length=256,blank=True)
    city = models.CharField(max_length=256,blank=True)
    class Meta:
        unique_together=("user","city")
   
    def __str__(self):
        return str(self.name+self.username)

class Designer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=256,blank=True)
    name = models.CharField(max_length=256,blank=True)
    designstyle = models.CharField(max_length=256,blank=True)
    designFeature = models.CharField(max_length=256,blank=True)
    mobile = models.CharField(max_length=256,blank=True)
    photo = models.URLField(max_length=256,blank=True)
    city = models.CharField(max_length=256,blank=True)
    class Meta:
        unique_together=("user","city")

    def __str__(self):
        return str(self.name+self.username)

