from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


# Create your views here.

def index(request) :
    return HttpResponse('Hello')


def some_url(request) :
    return HttpResponse('some url구현')

def graph(request):
    context = {'place': '서울'}
    # 템플릿에 context를 전달
    return render(request, 'polls/graph.html', context)