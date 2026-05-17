from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import Register_view,Register_detail
from .views import CompanyView
from .views import CarView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('company',CompanyView)
router.register('car',CarView)

urlpatterns = [
   path('register/',Register_view.as_view()),
   path('register/<int:pk>/',Register_detail.as_view()),
   path('login/',TokenObtainPairView.as_view()),
   path('login/refresh/',TokenRefreshView.as_view()),
   path('',include(router.urls)),
]
