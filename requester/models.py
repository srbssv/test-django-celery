from django.db import models

# Create your models here.

class Address(models.Model):
    url = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.url}'
    
    class Meta:
        verbose_name_plural = 'addresses'