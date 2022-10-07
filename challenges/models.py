from django.db import models

# Create your models here.
class Reward(models.Model):
    date_received = models.DateField(auto_now_add=True)
    credit_no = models.IntegerField()
    description = models.TextField(max_length=500)
    def __str__(self) -> str:
        return self.description

    class Meta:
        ordering = ['-date_received']


class Challenge(models.Model):
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    credits = models.IntegerField()
    description = models.TextField(max_length=500)
    rewards = models.ManyToManyField(Reward)
    def __str__(self) -> str:
        return self.name

class Winner(models.Model):
    challenge=models.ForeignKey(Challenge,on_delete=models.CASCADE)
    reward=models.ManyToManyField(Reward)
    def __str__(self):
        return self.User