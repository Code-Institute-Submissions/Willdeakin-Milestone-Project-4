from django.db import models

# Create your models here.


class products (models.Model):

    brand = models.CharField(max_length=254, null=True, blank=True)
    product	= models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description	= models.TextField()
    category = models.CharField(max_length=254, null=True, blank=True)
    serving	= models.CharField(max_length=254, null=True, blank=True)
    adjustable = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
