from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','email','company_name','phone_number','profile_image')
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'email': 'Email adres',
            'company_name': 'Nazwa firmy',
            'phone_number': 'Numer telefonu',
            'profile_image': 'Zdjęcie profilowe',
        }
