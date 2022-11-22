from django.db import models
from PIL import Image
# Create your models here.




class Portfolio(models.Model):
    category = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    
