from django.contrib import admin
from django.contrib.auth.models import User
# from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

from .models import Item, Story,Donateitem

admin.site.register(Item)
admin.site.register(Story)
admin.site.register(Donateitem)
admin.site.unregister(User)
# admin.site.unregister(Site)
admin.site.unregister(Group)