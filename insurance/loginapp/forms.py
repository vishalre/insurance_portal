from django import forms
from django.contrib.auth.models import User

from loginapp.models import detailsmodel

class details_form(forms.ModelForm):
    class Meta:
        model=detailsmodel
        fields="__all__"
