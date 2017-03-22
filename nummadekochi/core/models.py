from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    item_image = models.ImageField(upload_to='media')
    description = models.TextField(max_length=255)
    added_time = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Story(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.title