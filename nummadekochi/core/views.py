from django.shortcuts import render

from .models import Item, Story,Donateitem
from .forms import ItemForm,DonateForm

import PIL

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

def itemdonateview(request,id):
    item = Item.object.get(id=id)
    context ={'item1':item}
    return render(request,'core/donateform.html',context)

def donateview(request,id): 
    # item =Item.object.get(id=id)   
    form = DonateForm()
    if request.method == 'POST':

        form = DonateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DonateForm()

    return render(request,'core/donateform.html',{'form':form ,})
