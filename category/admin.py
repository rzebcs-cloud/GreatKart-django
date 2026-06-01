from django.contrib import admin

from category.models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'cat_slug': ('cat_name',)}
    list_display = ('cat_name', 'cat_slug', 'cat_image')
admin.site.register(Category, CategoryAdmin)