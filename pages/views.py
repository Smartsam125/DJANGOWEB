from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("hello,Smartsam")


# Create your views here.
