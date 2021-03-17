from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.startPage, name="startPage"),
    path('accounts/', include('accounts.urls')),
]