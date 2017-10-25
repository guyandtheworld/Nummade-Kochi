from django import forms
from django.core.exceptions import ValidationError

from .models import Item, Donateitem

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'item_image', 'description', 'fulfilled']


class DonateForm(forms.ModelForm):
    class Meta:
        model = Donateitem
        fields = ['quantity','donor','phone','address']

class StoryForm(forms.ModelForm):
	class Meta:
		model = Story
		fields = ['title','description','story_image']
