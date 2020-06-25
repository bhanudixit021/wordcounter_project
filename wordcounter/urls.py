
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage, name = 'home'),
    path('saify/',views.count, name = 'count'),
    path('bhanu/',views.about,name = 'about')
]
