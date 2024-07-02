# forms.py
from django import forms
from .models import Producte

class ProducteForm(forms.Form):
    producte = forms.ModelChoiceField(queryset=Producte.objects.all(), label="Selecciona un producte")
