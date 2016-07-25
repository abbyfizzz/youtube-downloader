from django.shortcuts import render
from django.hhtp import HttpResponse

def index(request):
    return HttpResponse("<h1>tst</h1>")
