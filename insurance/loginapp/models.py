from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# printf(timezone.now)
# Create your models here.
# TITLE_CHOICES = (
#     ('Swift', 'Swift'),
#     ('Ertiga', 'Ertiga'),
#     ('Baleno', 'Baleno'),
#     ('Breeza','Breeza'),
#     ('Ciaz','Ciaz')
# )
# AGE=(
# ('Under 1','Under 1'),
# ('1 to 2','1 to 2'),
# ('2 to 3','2 to 3'),
# ('3 to 4','3 to 4'),
# ('Over 4','Over 4')
# )

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete = 'cascade')
    license = models.IntegerField(default = 1231)
    address = models.CharField(max_length = 100, blank = True, default = 'place')
    city = models.CharField(max_length = 10, blank = True, default = 'place')
    country = models.CharField(max_length = 10, blank = True, default = 'place')
    zipcode = models.CharField(max_length = 10, blank = True, default = 'place')

    def __str__(self):
        return self.user.username

class detailsmodel(models.Model):
    userid = models.ForeignKey(User, on_delete= 'cascade')
    licnum = models.CharField(max_length=50)
    carImg = models.ImageField(upload_to='images/')
    speed=models.IntegerField()
    vechilemodel= models.CharField(max_length=10)
    ageofvechile=models.CharField(max_length=10,default='place')

    def __str__(self):
        return self.userid.username
