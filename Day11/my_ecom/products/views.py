from django.shortcuts import render
from django.http import HttpResponse

def products(request):
    return HttpResponse("Hello.. Welcome to our products Page")