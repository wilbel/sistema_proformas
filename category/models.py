from django.db import models

# Create your models here.

class Category(models.Model):
        name_category = models.CharField(max_length=20,unique=True)
        description_category = models.CharField(max_length=50, blank=True)

        class Meta:
                verbose_name='category'
                verbose_name_plural='categories'

        def __str__(self):
                return self.name_category
