from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("new/", views.new, name="new"),
    path("", views.create, name="create"),
]
