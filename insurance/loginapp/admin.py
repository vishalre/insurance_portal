from django.contrib import admin
from loginapp.models import detailsmodel,UserProfile,Otpgenerator,Claimdetails,logindetails
# Register your models here.

# admin.site.register(Login_details)
admin.site.register(detailsmodel)
admin.site.register(UserProfile)
admin.site.register(Otpgenerator)
admin.site.register(Claimdetails)
admin.site.register(logindetails)
