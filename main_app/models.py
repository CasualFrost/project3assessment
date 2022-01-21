from django.db import models

# Create your models here.
class Widget(models.Model):
    item = models.CharField(max_length=50)
    quantity = models.IntegerField
    
    def __str__(self):
        return self.item