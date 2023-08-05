from django.shortcuts import render



def news(request):
    """ A view to return the index page """
    return render(request, 'news/news.html')
