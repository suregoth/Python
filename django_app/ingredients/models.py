from django.db import models

class Cosmetics(models.Model):
    name = models.CharField(max_length=50)
    inci = models.CharField(max_length=50)