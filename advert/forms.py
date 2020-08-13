from django import forms
from advert.models import Advert


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['category',
                  'description',
                  'location',
                  'street',
                  'advantages',
                  'surroundings',
                  'area',
                  'no_of_rooms',
                  'price',
                  'image1',
                  'image2',
                  'image3']
        widgets = {
            'advantages': forms.CheckboxSelectMultiple,
            'surroundings': forms.CheckboxSelectMultiple,
        }
        labels = {
            'category': 'Rodzaj nieruchomości',
            'description': 'Opis nieruchomości',
            'location': 'Lokalizacja',
            'street': 'Ulica',
            'advantages': 'Zalety nieruchomości',
            'surroundings': 'Okolica',
            'area': 'Powierzchnia użytkowa',
            'no_of_rooms': 'Ilość pokoi',
            'price': 'Cena',
            'image1': 'Zdjęcie 1',
            'image2': 'Zdjęcie 2',
            'image3': 'Zdjęcie 3',
        }
