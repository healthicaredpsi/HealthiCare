from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=800)
    def __str__(self):
        return self.name

class Message(models.Model):
    value=models.CharField(max_length=1000000)
    date=models.DateTimeField(auto_now_add=True)
    user= models.CharField(max_length=1000000)
    room=models.ManyToManyField(Room)
    def __str__(self):
        return self.value
