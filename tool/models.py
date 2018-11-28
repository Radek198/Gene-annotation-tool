from django.db import models

# Create your models here.

class Genes(models.Model):
    Gname = models.CharField(max_length=255, null=True)
    annotation = models.CharField(max_length=255, null=True)



