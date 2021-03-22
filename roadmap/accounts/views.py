from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Profile
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
        else:
            errors = user_form.errors and profile_form.errors
            return render(request, 'accounts/edit.html', {'user_form': user_form, 'profile_form': profile_form, 'errors':errors})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'accounts/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def profile(request):
    model = Profile.objects.filter(user=request.user)
    modelUser = User.objects.filter(username=request.user)
    return render(request, 'accounts/profile.html', {'model':model, 'modelU':modelUser})