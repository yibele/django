from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello wordl, you are at the polls index")

def test(request):
    return HttpResponse('test')

