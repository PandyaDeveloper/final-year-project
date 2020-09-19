from django.db import models

# Create your models here.
class us(models.Model):
    Email = models.CharField(max_length=50,unique=True,primary_key=True,blank=False)
    password = models.CharField(max_length=20)
    otp = models.IntegerField(default=0000)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

class info(models.Model):
    email = models.ForeignKey(us,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=False)
    age = models.IntegerField(blank=True)
    number = models.TextField(blank=True)
    gender = models.CharField(max_length=6)

class postd(models.Model):
    pus = models.ForeignKey(us,on_delete=models.CASCADE)
    pti = models.CharField(max_length=500,blank=False)
    pde = models.TextField(blank=False)
    sen = models.CharField(max_length=10,blank=False)
