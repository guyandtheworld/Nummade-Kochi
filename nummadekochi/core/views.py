from django.shortcuts import render

from nummadekochi.core import models

def main(request):
    return render(request, 'core/main.html')

def about(request):
    return render(request, 'core/about.html')

def donate(request):
    return render(request, 'core/donate.html')

def stories(request):
    return render(request, 'core/stories.html')

def contact_us(request):
    return render(request, 'core/contact_us.html')