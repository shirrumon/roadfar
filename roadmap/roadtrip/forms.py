from django.forms import ModelForm
from .models import Category, Step
from django.contrib.auth.models import User


class Cat(ModelForm):
    class Meta:
        model = Category
        fields = ['target']


class Steping(ModelForm):
    class Meta:
        model = Step
        fields = ['category', 'name', 'description']
