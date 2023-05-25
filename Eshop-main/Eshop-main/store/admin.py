from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)



admin.site.register(Category,CategoryAdmin)


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone']
admin.site.register(Customer,AdminCustomer)


class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer']
admin.site.register(Order,AdminOrder)



