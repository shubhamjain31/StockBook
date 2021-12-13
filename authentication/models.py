from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    fullname                = models.CharField(max_length=20, blank=True, null=True)
    username                = models.CharField(max_length=20, unique=True)
    email                   = models.EmailField(unique=True)
    mobile                  = models.CharField(max_length=20, blank=True, null=True)
    first_name              = models.CharField(max_length=30, blank=True, null=True)
    last_name               = models.CharField(max_length=30, blank=True, null=True)
    password                = models.CharField(max_length=150)
     
    last_login              = models.DateTimeField(blank=True, null=True)
    last_logout             = models.DateTimeField(blank=True, null=True)
    date_joined             = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    ip_address              = models.CharField(max_length=100, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

class PasswordRecovery(models.Model):
    class Meta:
        verbose_name_plural = 'Password Recovery'

    username                    = models.CharField(max_length=100)
    reset_link                  = models.CharField(max_length=200)
    created_date                = models.DateTimeField(auto_now_add=True)
    ip_address                  = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username