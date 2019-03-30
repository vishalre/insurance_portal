from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TITLE_CHOICES = (
    ('Swift', 'Swift'),
    ('Ertiga', 'Ertiga'),
    ('Baleno', 'Baleno'),
    ('Breeza','Breeza'),
    ('ciaz','ciaz')
)

class detailsmodel(models.Model):
    licnum = models.CharField(max_length=50)
    carImg = models.ImageField(upload_to='images/')
    speed=models.IntegerField()
    vechilemodel= models.CharField(max_length=7, choices=TITLE_CHOICES)
