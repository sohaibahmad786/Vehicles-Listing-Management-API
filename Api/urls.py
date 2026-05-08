from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import Register_view,Register_detail
from .views import Search_view
from .views import Studentlist,Studentdetail
from .views import Task_listview,Task_detailview
from .views import Bookinglistview,AvailableSlotView
from .views import MessagelistView,Chatlistview
from .views import PersonViewSet
from .views import CompanyView
from .views import CarView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('person',PersonViewSet)
router.register('company',CompanyView)
router.register('car',CarView)

urlpatterns = [
   path('register/',Register_view.as_view()),
   path('register/<int:pk>/',Register_detail.as_view()),
   path('login/',TokenObtainPairView.as_view()),
   path('login/refresh/',TokenRefreshView.as_view()),
   path('search/',Search_view.as_view()),
   path('student/',Studentlist.as_view()),
   path('student/<int:pk>/',Studentdetail.as_view()),
   path('task/',Task_listview.as_view()),
   path('task/<int:pk>/',Task_detailview.as_view()),
   path('book/',Bookinglistview.as_view()),
   path('available/',AvailableSlotView.as_view()),
   path('message/',MessagelistView.as_view()),
   path('chat/',Chatlistview.as_view()),
   path('',include(router.urls)),
]