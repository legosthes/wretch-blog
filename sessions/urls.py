from django.urls import path
from . import views

app_name = "sessions"

urlpatterns = [
    path("new/", views.new, name="new"),
]
