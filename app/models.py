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


    def __str__(self):
        return self.name