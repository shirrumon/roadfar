from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.CharField(User, max_length=100)

    def __str__(self):
        return self.target
    pass


class Step(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Img(models.Model):
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)