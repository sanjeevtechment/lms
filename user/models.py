from django.db import models

# Create Users models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    mobile = models.CharField(max_length=20)
    bio = models.TextField()
    date_of_birth = models.DateField()
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    status = models.CharField(max_length=20, choices=( ('active', 'active'), ('inactive', 'inactive'), ('pending', 'pending'), ('hold', 'hold'), ('terminate', 'terminate') ))
    is_active = models.BooleanField(default=True)
    is_active_action_date = models.DateTimeField(auto_now=True)