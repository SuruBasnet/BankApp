from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=300,unique=True)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    image = models.FileField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Account(models.Model):
    account_name = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    mobile_no = models.CharField(max_length=20)
    ac_no = models.CharField(max_length=200,unique=True)
    cheque_no = models.CharField(max_length=200,unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)

class Bank(models.Model):
    name = models.CharField(max_length=200,unique=True)
    short_name = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)

class Statement(models.Model):
    account = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    amount = models.FloatField()
    type = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=20)
    description = models.TextField()
    withdrawn_by = models.CharField(max_length=200,null=True)
    bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    cheque_no = models.CharField(max_length=200,null=True)
    deposit_by = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)
