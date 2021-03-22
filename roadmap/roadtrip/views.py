from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import Steping, Cat
from .models import Category, Step, Img


def startPage(request):
        if request.user.is_authenticated:
                model = Img.objects.all()
                return render(request, 'roadtrip/startpage.html', {'model' : model})
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
        model = Category
        form.fields['category'].queryset = model.objects.filter(owner=request.user)
    return render(request, 'roadtrip/addtarg.html', {'form' : form})


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


def delete_unit(request, pk):
    set = Step.objects.filter(pk=pk)
    set.delete()
    return render(request, 'roadtrip/addsucces.html')


def delete_cat(request, pk):
    set = Category.objects.filter(pk=pk)
    set.delete()
    return render(request, 'roadtrip/myroads.html')


def post_edit(request, pk):
    post = get_object_or_404(Step, pk=pk)
    if request.method == "POST":
        form = Steping(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('myRoads')
    else:
        form = Steping(instance=post)
    return render(request, 'roadtrip/addtarg.html', {'form': form})