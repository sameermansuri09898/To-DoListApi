from rest_framework import routers
from django.urls import path
from .views import StudentCreationsClass,LoginFunctionaluity,LogoutUser



urlpatterns=[
  path('Registration/',StudentCreationsClass.as_view(),name='StudentRegistration'),
  path('Account/LOgin',LoginFunctionaluity.as_view(),name='login'),
  path('Account/Logout',LogoutUser.as_view(),name='logout'),
]
