from django.urls import path
from django.shortcuts import render
from django.contrib import admin


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("about/", about),
]
