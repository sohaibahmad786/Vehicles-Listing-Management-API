from django.shortcuts import render
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import permissions
from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from datetime import datetime, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from rest_framework .viewsets import ModelViewSet

from .models import Register
from .serializer import Register_serializer
from .models import Company
from .serializer import Company_serializer
from .models import Cars
from .serializer import Cars_serializer

    
class Register_view(generics.ListCreateAPIView):
    serializer_class=Register_serializer
    permission_classes=[AllowAny]
    def get_queryset(self):
        login_user=self.request.user

        if not login_user.is_authenticated:
            return Register.objects.none()

        if login_user.Role=='admin':
            return Register.objects.all()
        else:
            return Register.objects.filter(id=login_user.id)
    
class Register_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Register.objects.all()
    serializer_class=Register_serializer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticated]


class CompanyView(ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=Company_serializer

class CarView(ModelViewSet):
    queryset=Cars.objects.all()
    serializer_class=Cars_serializer
    permission_classes=[IsAuthenticated]

    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['name','company__name']
    filterset_fields=['fuel_type','color','company']
    ordering_fields=['price','model']
# Create your views here.





