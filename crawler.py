import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.weather.go.kr/weather/observation/currentweather.jsp")
soup = BeautifulSoup(source.content, 'html.parser')
print(soup.text)