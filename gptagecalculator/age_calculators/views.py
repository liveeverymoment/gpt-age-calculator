from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def event_age(request):
    return HttpResponse('event age is today.')
