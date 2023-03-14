from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name_category',)}
    list_display = ('name_category','slug')


admin.site.register(Category,CategoryAdmin)



#admin.site.register(Category)