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
from .models import Search_data
from .serializer import Search_serializer
from .models import Students
from .serializer import Student_serializer
from .models import Task
from .serializer import Task_serializer
from .models import Booking
from .serializer import Booking_serializer
from .models import Message
from .serializer import Message_serializer
from .models import Person
from .serializer import Person_serializer
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

class Search_view(generics.ListCreateAPIView):
    queryset=Search_data.objects.all()
    serializer_class=Search_serializer
    filter_backends=[filters.SearchFilter]
    search_fields=['Name','About']
class Studentlist(generics.ListCreateAPIView):
    queryset=Students.objects.all()
    serializer_class=Student_serializer
class Studentdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Students.objects.all()
    serializer_class=Student_serializer

class Task_listview(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=Task_serializer
class Task_detailview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=Task_serializer

class Bookinglistview(generics.ListCreateAPIView):
    serializer_class=Booking_serializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AvailableSlotView(APIView):
    def get(self,request):
        date=request.GET.get('date')
        booked_times=Booking.objects.filter(date=date).values_list('time',flat=True)
        all_slots=['9:00:00','10:00:00','11:00:00','12:00:00','1:00:00','2:00:00','3:00:00']
        available=[slot for slot in all_slots if slot not in booked_times]
        
        return Response({
            'available_slot':available
        })
     
class MessagelistView(ListCreateAPIView):
    serializer_class=Message_serializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)  

class Chatlistview(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        user=request.user
        reciever_id=request.GET.get('reciever')
        messages=Message.objects.filter(
            Q(sender=user,reciever_id=reciever_id) | Q(sender_id=reciever_id,reciever=user)
        ).order_by('created_at')
        serializer=Message_serializer(messages, many=True)
        return Response(serializer.data)


class PersonViewSet(ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=Person_serializer

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





