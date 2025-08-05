from django.urls import path

# views 差不多是前端的部分，html, css, javascript
# 用資料夾創立模組
from . import views

# urlpatterns的名字是固定的
urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    path("contact/", views.contact),
]
