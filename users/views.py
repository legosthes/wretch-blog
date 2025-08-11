from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def new(request):
    return render(request, "users/new.html")


@require_POST
def create(request):
    username = request.POST["username"]
    password = request.POST["password"]

    if username != "" and password != "":
        user = User.objects.create_user(username=username, password=password)
        if user:
            # 認證信可以加這裡
            messages.success(request, "Registered successfully!")
            return redirect("articles:index")
        else:
            messages.error(request, "Please try again.")
            return redirect("users:new")

    else:
        return redirect("users:new")
