from django import forms
from .models import RealEstate, Province, City, District

class RealEstateForm(forms.ModelForm):
    class Meta:
        model = RealEstate
        fields = ['province', 'city', 'district', 'price', 'room', 'area', 'year', 'floor', 'parking', 'elevator',
                  'warehouse', 'document', 'description', 'status']
        widgets = {
            'province': forms.Select(attrs={'id': 'province'}),
            'city': forms.Select(attrs={'id': 'city'}),
            'district': forms.Select(attrs={'id': 'district'})
        }
