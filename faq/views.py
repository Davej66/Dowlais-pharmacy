from django.shortcuts import render



def faq(request):
    """ A view to return the index page """
    return render(request, 'faq/faq.html')
