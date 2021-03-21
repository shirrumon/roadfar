from django.forms import ModelForm
from .models import Category, Step


class Cat(ModelForm):
    class Meta:
        model = Category
        fields = ['target']


class Steping(ModelForm):
    class Meta:
        model = Step
        fields = ['category', 'name', 'description']