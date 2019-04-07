from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TITLE_CHOICES = (
    ('Swift', 'Swift'),
    ('Ertiga', 'Ertiga'),
    ('Baleno', 'Baleno'),
    ('Breeza','Breeza'),
    ('Ciaz','Ciaz')
)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete = 'cascade')
    address = models.CharField(max_length = 100, blank = True, default = 'place')
    city = models.CharField(max_length = 10, blank = True, default = 'place')
    country = models.CharField(max_length = 10, blank = True, default = 'place')
    zipcode = models.CharField(max_length = 10, blank = True, default = 'place')

    def __str__(self):
        return self.user.username


class detailsmodel(models.Model):
    licnum = models.CharField(max_length=50)
    carImg = models.ImageField(upload_to='images/')
    speed=models.IntegerField()
    vechilemodel= models.CharField(max_length=7, choices=TITLE_CHOICES)

    def __str__(self):
        return self.user.username
