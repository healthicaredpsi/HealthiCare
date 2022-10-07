from django.db import models

# Create your models here.
class Breath(models.Model):
    duration = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.duration

    class Meta:
        ordering = ['-time']


class Meditation(models.Model):
    duration = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.duration

    class Meta:
        ordering = ['-time']