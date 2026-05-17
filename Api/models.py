from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Register(AbstractUser):
    class Meta:
        verbose_name = "Register"          
        verbose_name_plural = "Register"
    ROLE_CHOICES=(
        ('admin','Admin'),
        ('user',"User"),
    )
    Role=models.CharField(choices=ROLE_CHOICES,default='user')
    def __str__(self):
        return self.username
    

class Company(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name
        
class Cars(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='cars')
    name=models.CharField()
    model=models.IntegerField()
    color=models.CharField()
    Type=(
        ('diesel','Diesel'),
        ('petrol','Petrol'),
        ('cng','CNG'),
    )
    fuel_type=models.CharField(choices=Type,default='diesel')
    price=models.IntegerField()

    def __str__(self):
        return self.name
# Create your models here.
