from django.db import models

# Create your models here.
from django.urls import reverse


# changed 

class Tea(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()

    def get_price(self):
        return self.price

    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})