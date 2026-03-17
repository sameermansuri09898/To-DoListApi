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

class todolist(models.Model):
    user = models.ForeignKey(BaseRegistration, on_delete=models.CASCADE)
    items_name=models.CharField(max_length=100)
    Category=models.CharField(max_length=30)
    updated_now=models.DateField(auto_now_add=True)
    created_now=models.DateField(auto_now=True)

    def __str__(self):
        return super().__str__()
