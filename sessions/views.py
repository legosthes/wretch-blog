from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def new(request):
    return render(request, "sessions/new.html")


@require_POST
def create(request):
    pass
