from django.db import models
from django.urls import reverse

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('product_lis_by_category',args=[self.slug])

class Product(models.Model):
    Category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%/%/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        index_together= (('id', 'slug'),)
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

    def get_url_id(self):
        return reverse('add_cart', args=[self.id])
