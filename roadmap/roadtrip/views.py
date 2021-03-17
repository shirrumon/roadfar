from django.shortcuts import render


def startPage(request):
    return render(request, 'roadtrip/startpage.html')