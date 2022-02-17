from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ExtendedUser(AbstractUser):
    
    email = models.EmailField(unique=True, blank=False, max_length=255, verbose_name='email') 

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'