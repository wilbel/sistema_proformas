from django.db import models


# Create your models here.

class Customer(models.Model):
    name_customer = models.CharField(max_length=200,unique=True)
    ced_ruc = models.CharField(max_length=15,blank=True)
    description_customer = models.TextField(max_length=500,blank=True)
    email_customer = models.CharField(max_length=50,blank=True)
    direction = models.TextField(max_length=200,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_customer