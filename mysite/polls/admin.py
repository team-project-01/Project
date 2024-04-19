from django.contrib import admin
from .models import *

admin.site.register(ForecastData)
admin.site.register(RainPercent)
admin.site.register(Wind)