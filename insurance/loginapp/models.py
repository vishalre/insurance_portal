from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Otpgenerator(models.Model):
    mailid = models.CharField(max_length=40,primary_key=True)
    otp = models.IntegerField()


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete = 'cascade')
    license = models.IntegerField(default = 1231)
    licenseplate = models.CharField(max_length = 50,default = 'licenseplate')
    profession = models.CharField(max_length = 100, default = 'job')
    address = models.CharField(max_length = 100, blank = True, default = 'place')
    city = models.CharField(max_length = 10, blank = True, default = 'place')
    country = models.CharField(max_length = 10, blank = True, default = 'place')
    zipcode = models.CharField(max_length = 10, blank = True, default = 'place')

    def __str__(self):
        return self.user.username

class detailsmodel(models.Model):
    userid = models.ForeignKey(User, on_delete= 'cascade')
    licnum = models.CharField(max_length=50)
    lplate = models.CharField(max_length = 50,default = 'lnum')
    carImg = models.ImageField(upload_to='images/')
    speed=models.IntegerField()
    vechilemodel= models.CharField(max_length=10)
    ageofvechile=models.CharField(max_length=10,default='place')
    damagedpart = models.CharField(max_length = 10,default='test')
    # testmodel = models.ManyToManyField(Parts)

    def __str__(self):
        return self.userid.username

#
# class Parts(models.Model):
#     desc = models.CharField(max_length=300)
