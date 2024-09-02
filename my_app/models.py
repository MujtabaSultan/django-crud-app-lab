from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

class Modification(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('modification-detail', kwargs={'pk': self.id})

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=250)
    modifications = models.ManyToManyField(Modification)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
       
        return reverse('car-detail', kwargs={'car_id': self.id})