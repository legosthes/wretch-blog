from django.urls import path
from django.contrib import admin
from .views import home, about

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("about/", about),
]
