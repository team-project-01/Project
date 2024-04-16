from django.contrib import admin
from .models import Question, forecastData, Rainpercent, Wind

admin.site.register(Question)
admin.site.register(forecastData)
admin.site.register(Rainpercent)
admin.site.register(Wind)