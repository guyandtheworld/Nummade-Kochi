from django.shortcuts import render

from .models import Item, Story
from .forms import ItemForm

def main(request):
    return render(request, 'core/main.html')

def about(request):
    return render(request, 'core/about.html')

def donate(request):
    items = list(item for item in Item.objects.all()
                                        if not item.fulfilled)
    return render(request, 'core/donate.html',
                    {'items': items})

def stories(request):
    stories = Story.objects.all()
    return render(request, 'core/stories.html', 
                    {'stories': stories})

def contact_us(request):
    return render(request, 'core/contact_us.html') 