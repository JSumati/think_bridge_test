from django.db import models
from stdimage import StdImageField

class inventory(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    # image = models.ImageField(unique=True, upload_to='images/')
    image = StdImageField(upload_to='images/', variations={
        'thumbnail': {"width": 100, "height": 100, "crop": True}
    })