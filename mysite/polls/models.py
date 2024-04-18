
from django.db import models

class forecastData(models.Model): #날짜 별 온도 데이터 저장
    fcstDate = models.CharField(max_length=8)
    fcstTime = models.CharField(max_length=2)
    fcstValue = models.CharField(max_length=10)
    fnx = models.CharField(max_length=5)
    fny = models.CharField(max_length=5)
    index_num = models.CharField(max_length=5, default='00000')
    indexname = models.CharField(max_length=10, default='00000')
    def __str__(self):
        return f'{self.indexname}의 {self.fcstDate[:4]}년 {self.fcstDate[4:6]}월 {self.fcstDate[6:]}일 {self.fcstTime}시 온도(도씨)'
    
        
class Rainpercent(models.Model): #날짜 별 강수확률 데이터 저장
    fcstDate = models.CharField(max_length=8)
    fcstTime = models.CharField(max_length=2)
    fcstValue = models.CharField(max_length=10)
    fnx = models.CharField(max_length=5)
    fny = models.CharField(max_length=5)
    index_num = models.CharField(max_length=5, default='00000')
    indexname = models.CharField(max_length=10, default='00000')
    def __str__(self):
        return f'{self.indexname}의 {self.fcstDate[:4]}년 {self.fcstDate[4:6]}월 {self.fcstDate[6:]}일 {self.fcstTime}시 강수량(mm)'
    
class Wind(models.Model): #날짜 별 풍속 데이터 저장
    fcstDate = models.CharField(max_length=8)
    fcstTime = models.CharField(max_length=2)
    fcstValue = models.CharField(max_length=10)
    fnx = models.CharField(max_length=5)
    fny = models.CharField(max_length=5)
    index_num = models.CharField(max_length=5, default='00000')
    indexname = models.CharField(max_length=10, default='00000')
    def __str__(self):

        return f'{self.indexname}의 {self.fcstDate[:4]}년 {self.fcstDate[4:6]}월 {self.fcstDate[6:]}일 {self.fcstTime}시 풍속(m/s)'
