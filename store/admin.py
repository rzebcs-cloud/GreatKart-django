from django.contrib import admin

from store import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'is_avalible', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    
admin.site.register(models.Product, ProductAdmin)