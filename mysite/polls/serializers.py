from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from .models import *

class forecastDataSerializer(ModelSerializer):
    class Meta:
        model = ForecastData
        fields = '__all__' 


class RainPercentSerializer(ModelSerializer):
    class Meta:
        model = RainPercent
        fields = "__all__"


class WindSerializer(ModelSerializer):
    class Meta:
        model = Wind
        fields = "__all__"
