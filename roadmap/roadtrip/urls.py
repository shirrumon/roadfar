from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.startPage, name="startPage"),
    path('add/', views.addTarg, name="addTarg"),
    path('addcat/', views.addCat, name="addCat"),
    path('success/', views.addSuccess, name="addSuccess"),
    path('roads/', views.myRoads, name="myRoads"),
    path('roads/<int:pk>/', views.unit_detail, name="unit_detail"),
    path('accounts/', include('accounts.urls')),
]