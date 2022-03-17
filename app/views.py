from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Raja(request):
    return HttpResponse('Raja first view')

def django(request):
    return HttpResponse('<marquee><h1> first view</h1></marquee>')
