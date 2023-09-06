from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    country = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title
