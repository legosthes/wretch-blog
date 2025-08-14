from django.urls import path

from . import views
from articles.views import index


app_name = "payments"

urlpatterns = [
    path("new/", views.new, name="new"),
    path("", views.index, name="index"),
]
