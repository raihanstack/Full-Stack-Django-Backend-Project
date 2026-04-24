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