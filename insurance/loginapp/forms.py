from django import forms
from django.contrib.auth.models import User
from loginapp.models import Login_details

class User_form(forms.ModelForm):
    class Meta:
        model = Login_details
        fields = "__all__"
