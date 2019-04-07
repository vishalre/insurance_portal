from django.contrib import admin
from loginapp.models import detailsmodel,UserProfile
# Register your models here.

# admin.site.register(Login_details)
admin.site.register(detailsmodel)
admin.site.register(UserProfile)
