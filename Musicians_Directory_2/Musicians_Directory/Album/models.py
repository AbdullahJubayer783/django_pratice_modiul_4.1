from django.db import models
from musician.models import Musicians
# Create your models here.
class Albums(models.Model):
    name = models.CharField(max_length=60)
    release_date = models.DateField(auto_now_add=True)
    MY_CHOICES = (
        ('1', ' 1 star'),
        ('2', ' 2 star'),
        ('3', ' 3 star'),
        ('4', ' 4 star'),
        ('5', ' 5 star'),
    )
    
    Rating = models.CharField(max_length=10, choices=MY_CHOICES)
    musician = models.ForeignKey(Musicians ,on_delete=models.CASCADE)