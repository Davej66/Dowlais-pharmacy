from django.http import HttpResponse
from django.shortcuts import render

def building(request):
    return render(request, 'building.html')


def cas(request):
    return render(request, 'cas.html')


def flu(request):
    return render(request, 'flu.html')

