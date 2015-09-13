from django.db import models


class Meal(models.Model):
    """
    stores all info relative to a meal:
    name
    url
    image
    nutritional info
    """
    url = models.CharField(max_length=500, primary_key='True')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
