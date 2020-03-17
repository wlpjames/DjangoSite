# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    shortDesc = models.CharField(max_length=100)
    description = models.TextField()
    thumb = image = models.ImageField(upload_to='')
    image = models.ImageField(upload_to="")
    
