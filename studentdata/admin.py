from django.contrib import admin
from django.db import models
from .models import User
# Register your models here.
@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')