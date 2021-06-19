from django.db import models

# Create your models here.

class Car(models.Model):
    producer = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    year_of_release = models.IntegerField()
    transmission = models.SmallIntegerField(choices=[('M', 'manual'), ('A', 'automatic'), ('R', 'robot')])
    color = models.CharField(max_length=255)
