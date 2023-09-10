from django.http import HttpResponse
from django.shortcuts import render

def building(request):
    return render(request, 'building.html')


def cas(request):
    return render(request, 'cas.html')


def beacons(request):
    return render(request, 'beacons.html')

def dowlais(request):
    return render(request, 'dowlais.html')

def georgetown(request):
    return render(request, 'georgetown.html')

def keir(request):
    return render(request, 'keir.html')

def lewis(request):
    return render(request, 'lewis.html')

def flu(request):
    return render(request, 'flu.html')




