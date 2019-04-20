import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','insurance.settings')

import django
django.setup()


from faker import Faker
from loginapp.models import detailsmodel,UserProfile
from django.contrib.auth.models import User
import random

fakegen = Faker()
# def test():
#     for i in range(10):
#         fake_firstname = fakegen.first_name()
#         fake_lastname = fakegen.last_name()
#         fake_username = fakegen.user_name()
#         fake_email = fakegen.email()
#         t = User.objects.get_or_create(username = fake_username,first_name = fake_firstname,last_name = fake_lastname,email = fake_email)
#         # print(fake_username,fake_firstname,fake_lastname)

# def popu_user():
#     t = User.objects.all()
#     for i in range(len(t)):
#         fake_city = fakegen.city()
#         fake_country = fakegen.country()
#         fake_addr = fakegen.address()
#         fake_zip = fakegen.zipcode()
#         up = UserProfile.objects.get(user = t[i])
#         up.city = fake_city
#         up.address = fake_addr
#         up.country = fake_country
#         up.zipcode = fake_zip
#         up.save()
#         print(i)

def popu_user():
    t = User.objects.all()
    for i in range(len(t)):
        fake_job = fakegen.job()
        fake_plate = fakegen.license_plate()

        # fake_plate = fakegen.address()
        up = UserProfile.objects.get(user = t[i])
        up.licenseplate = fake_plate
        # up.profession = fake_job
        up.save()
        print(i)

popu_user()
