
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class forecastData(models.Model): #날짜 별 온도 데이터 저장
    fcstDate = models.CharField(max_length=8)
    fcstTime = models.CharField(max_length=2)
    fcstValue = models.CharField(max_length=10)
    def __str__(self):
        return f'{self.fcstDate[:4]}년 {self.fcstDate[4:6]}월 {self.fcstDate[6:]}일 {self.fcstTime}시 온도(도씨)'
    
class Rainpercent(models.Model): #날짜 별 강수확률 데이터 저장
    fcstDate = models.CharField(max_length=8)
    fcstTime = models.CharField(max_length=2)
    fcstValue = models.CharField(max_length=10)
    def __str__(self):
        return f'{self.fcstDate[:4]}년 {self.fcstDate[4:6]}월 {self.fcstDate[6:]}일 {self.fcstTime}시 강수확률(%)'
    
class Wind(models.Model): #날짜 별 풍속 데이터 저장
    fcstDate = models.CharField(max_length=8)
    fcstTime = models.CharField(max_length=2)
    fcstValue = models.CharField(max_length=10)
    def __str__(self):
        return f'{self.fcstDate[:4]}년 {self.fcstDate[4:6]}월 {self.fcstDate[6:]}일 {self.fcstTime}시 풍속(m/s)'


