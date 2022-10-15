from django.db import models

# Create your models here.
class Station(models.Model):
    code = models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Train(models.Model):
    origin=models.ForeignKey(Station,on_delete=models.CASCADE,related_name="departures")
    destination=models.ForeignKey(Station,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"

class Passenger(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    trains=models.ManyToManyField(Train,blank=True,related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
