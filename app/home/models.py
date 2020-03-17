from django.db import models

# Create your models here.
class Index_Slider(models.Model):

    heading = models.CharField(max_length=255)
    desc = models.TextField(max_length=512)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='img/')
    active = models.BooleanField(default=True)
    link = models.URLField(max_length=255)

"""
class Page_Contents(models.Model):

	name models.CharField(max_length)

"""