from django.shortcuts import render


def new(request):
    return render(request, "payments/new.html")


def index(request):
    pass
