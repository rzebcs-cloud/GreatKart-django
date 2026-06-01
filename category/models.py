from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_slug = models.SlugField(max_length=100, unique=True)
    cat_description = models.TextField(blank=True, null=True)
    cat_image = models.ImageField(upload_to='photos/category_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    #to get urls for the category display in the context processor
    
    def get_url(self):
        return reverse('product_by_category', args=[self.cat_slug])

    def __str__(self):
        return self.cat_name