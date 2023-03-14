from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
     list_display = ('name_customer','ced_ruc','description_customer','email_customer','direction','modified_date')
   



admin.site.register(Customer,CustomerAdmin)


