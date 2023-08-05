from django.shortcuts import render



def services(request):
    """ A view to return the index page """
    return render(request, 'services/services.html')
