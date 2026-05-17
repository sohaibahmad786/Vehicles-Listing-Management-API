from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import Register
from .models import Company
from .models import Cars
        

class Register_serializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['username','Role','email','password','id']
        
    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)

class Cars_serializer(serializers.ModelSerializer):
    class Meta:
        model=Cars
        fields='__all__'
    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError("Price Can't be zero or less than zero")

class Company_serializer(serializers.ModelSerializer):
    cars=Cars_serializer(many=True,read_only=True)
    class Meta:
        model=Company
        fields=['id','name','cars']
