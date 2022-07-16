from django import views
from django.urls import path
from . import views

urlpatterns = [
    # '' is for home page
    path('', views.index, name='index'),

    # 'add' is for showing the page to add record
    path('add', views.add, name='add'),

    # url to add student to database
    path('addStudent', views.addStudent, name='addStudent'),

    # url to search for a student
    path('searchDB', views.searchDB, name='searchDB'),
]