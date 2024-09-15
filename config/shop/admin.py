from django.contrib import admin
from shop.models import product 
from shop.models import Catagory
# Register your models here.

admin.site.register(product)
admin.site.register(Catagory)
# admin.site.register(Category)