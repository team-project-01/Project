import csv
import pandas as pd
from polls.models import Observation

def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='cp949') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def save_to_model(data):
    for item in data:
        Observation.objects.create(
            fcstYear = item['fcstYear'],
            fcstMonth = item['fcstMonth'],
            fcstDate = item['fcstDate'],
            fcstValue = item['fcstValue'],
        )
