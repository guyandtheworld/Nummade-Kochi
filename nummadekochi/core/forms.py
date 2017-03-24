from django import forms
from django.core.exceptions import ValidationError

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'item_image', 'description', 'fulfilled']