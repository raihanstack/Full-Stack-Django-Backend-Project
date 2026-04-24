from datetime import datetime
import os
from django.db import models

def upload_loaction(instance, filename):
    filebase, extension = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return 'product_images/%s/%s.%s' % (
        instance.name,
        timestamp,
        extension.replace('.', '')
    )


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to=upload_loaction, blank=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name + " " + str(self.quantity)

    def total(self):
        return self.product.price * self.quantity