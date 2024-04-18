from django.contrib import admin
from .models import forecastData, Rainpercent, Wind

admin.site.register(forecastData)
admin.site.register(Rainpercent)
admin.site.register(Wind)