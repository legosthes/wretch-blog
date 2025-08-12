from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as logout_user


# Create your views here.
def new(request):
    return render(request, "sessions/new.html")


@require_POST
def create(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)

    if user:
        # 做session和cookie出來
        login(request, user)
        messages.success(request, "Login successful.")
        return redirect("articles:index")
    else:
        messages.error(request, "Login unsuccessful.")
        return redirect("sessions:new")


@require_http_methods(["DELETE"])
# 名字不能一樣，否則會stack overflow
def logout(request):
    logout_user(request)
    # 因為我用 htmx 所以我的 target 設定 navbar，那就會全部被換掉
    # 他只針對我指定的地方做修改，這才是為什麼我可以只render navbar.html 而不是整個 default
    # return redirect ("sessions:new")
    return render(request, "shared/navbar.html")
