from django.contrib import admin
from .models import BaseRegistration

@admin.register(BaseRegistration)

class BaseRegistrationAdmin(admin.ModelAdmin):
  list_display=['email']
# Register your models here.
