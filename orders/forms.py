from django import forms
from .models import Order
from django.db import models


SNACK = 'S'
LUNCH = 'L'
TIMES = ((SNACK, 'Snack'),
         (LUNCH, 'Lunch')
         )
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'collection', 'homeroom', 'notes_to_Canteen']
