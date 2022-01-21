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

class Drop(models.Model):
    name            = models.CharField(max_length=120, unique=True)
    created_date    = models.DateField(auto_now_add=True)
    ip_address      = models.CharField(max_length=100, blank=True, null=True)
    session_user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='session_user_drop')

    def __str__(self):
        return self.name

class Product(models.Model):
    name            = models.CharField(max_length=120, unique=True)
    sortno          = models.PositiveIntegerField()
    created_date    = models.DateField(auto_now_add=True)
    ip_address      = models.CharField(max_length=100, blank=True, null=True)
    session_user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='session_user_product')

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier            = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    design              = models.CharField(max_length=50)
    color               = models.CharField(max_length=50)
    buyer               = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    season              = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    drop                = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True)
    status              = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date        = models.DateField(auto_now_add=True)
    ip_address          = models.CharField(max_length=100, blank=True, null=True)
    session_user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='session_user_order')

    def __str__(self):
        return self.product.name