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
    
class Search_data(models.Model):
    Name=models.CharField()
    About=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Students(models.Model):
    name=models.CharField()
    rollno=models.IntegerField()
    city=models.CharField()
    email=models.EmailField()
    age=models.IntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    title=models.CharField()
    description=models.TextField()
    scheduled_time=models.DateTimeField()
    is_complete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField()
    date=models.DateField()
    time=models.TimeField()
    is_booked=models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name}-{self.date}"


class Message(models.Model):
    sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='sent_message')
    reciever=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='recieve_messages')
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}\n{self.reciever}"
    

class Person(models.Model):
    name=models.CharField()
    city=models.CharField()
    email=models.EmailField()

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
