from django.db import models

class inventory(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=100)

class Meta:
    db_table = 'inventory'
    constraints = [
        models.UniqueConstraint(fields=['image'], name='image')
    ]
