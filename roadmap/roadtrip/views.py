from django.http import HttpResponseRedirect
from django.shortcuts import render


def startPage(request):
        if request.user.is_authenticated:
                return render(request, 'roadtrip/startpage.html')
        else:
                return HttpResponseRedirect('accounts/login')