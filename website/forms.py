# from django.forms import ModelForm
from .models import Quotation
from django import forms

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['first_name', 
                  'last_name',
                  'email',
                  'mobile',
                  'address',
                  'home_appliance',
                  'home_appliance_maker',
                  'home_appliance_model_number',
                  'home_appliance_problem',
                  ]
        
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 75px; width: 200px'}),
            'home_appliance_problem': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 75px; width: 200px'}),
        }