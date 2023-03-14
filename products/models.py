from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.CharField(max_length=200,unique=True)
    description = models.TextField(max_length=500,blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=6)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    categoria = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

