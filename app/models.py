from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Supplier(models.Model):
    user  		 	= models.OneToOneField(User, on_delete=models.CASCADE)
    name  		 	= models.CharField(max_length=120, unique=True)
    address 	 	= models.CharField(max_length=220)
    created_date 	= models.DateField(auto_now_add=True)
    ip_address      = models.CharField(max_length=100, blank=True, null=True)
    session_user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='session_user')

    def __str__(self):
        return self.name

class Buyer(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    name            = models.CharField(max_length=120, unique=True)
    address         = models.CharField(max_length=220)
    created_date    = models.DateField(auto_now_add=True)
    ip_address      = models.CharField(max_length=100, blank=True, null=True)
    session_user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='session_user_buyer')

    def __str__(self):
        return self.name

class Season(models.Model):
    name            = models.CharField(max_length=120, unique=True)
    description     = models.CharField(max_length=220)
    created_date    = models.DateField(auto_now_add=True)
    ip_address      = models.CharField(max_length=100, blank=True, null=True)
    session_user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='session_user_season')

    def __str__(self):
        return self.name