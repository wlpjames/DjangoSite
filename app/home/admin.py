from django.contrib import admin

# Register your models here.
from django.contrib import admin
from home.models import Index_Slider

class SliderAdmin(admin.ModelAdmin):
	pass

admin.site.register(Index_Slider, SliderAdmin)