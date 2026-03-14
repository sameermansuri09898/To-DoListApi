from rest_framework import routers
from django.urls import path
from .views import StudentCreationsClass



urlpatterns=[
  path('Registration/',StudentCreationsClass.as_view(),name='StudentRegistration')
]
