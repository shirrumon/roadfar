from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import Steping, Cat
from .models import Category, Step


def startPage(request):
        if request.user.is_authenticated:
                return render(request, 'roadtrip/startpage.html')
        else:
                return HttpResponseRedirect('accounts/login')


def addSuccess(request):
        return render(request, 'roadtrip/addsucces.html')


def myRoads(request):
    model = Category.objects.filter(owner=request.user)
    return render(request, 'roadtrip/myroads.html', {'model' : model})


def addTarg(request):
    if request.method == "POST":
        form = Steping(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'roadtrip/addsucces.html')
        else:
            print(form.errors)
    else:
        form = Steping()
    return render(request, 'roadtrip/addtarg.html', { 'form' : form})


def addCat(request):
    if request.method == "POST":
        form = Cat(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.owner = request.user
            cat.save()
            return render(request, 'roadtrip/addsucces.html')
        else:
            print(form.errors)
    else:
        form = Cat()
    return render(request, 'roadtrip/addcat.html', { 'form' : form})


def unit_detail(request, pk):
    set = get_object_or_404(Category, pk=pk)
    unit = Step.objects.filter(category=set)
    return render(request, 'roadtrip/roadunit.html', {'unit' : unit})