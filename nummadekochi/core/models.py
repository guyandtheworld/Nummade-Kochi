from django.db import models
from django.conf import settings

class Item(models.Model):
    name = models.CharField(max_length=50)
    item_image = models.ImageField(upload_to='')
    description = models.TextField(max_length=255)
    added_time = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Story(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1024)
    story_image = models.ImageField(null=True)

    def __str__(self):
        return self.title