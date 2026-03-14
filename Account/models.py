from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseRegistration(AbstractUser):
  Address=models.CharField(max_length=50)
  gender=models.CharField(max_length=2)

  USERNAME_FIELD = 'email'  
  REQUIRED_FIELDS = ['username']  # still needed for admin

  email = models.EmailField(unique=True)  # unique login

  def __str__(self):
        return self.email

