from django.urls import path
from . import views

# 給他別名才不會跟上面打架
from comments import views as comment_views

app_name = "articles"

urlpatterns = [
    # 這些urlpatterns是有順序的，如果<id>在前面，就會被吃掉
    # 所以才在id前加int，說是整數才可以通過
    path("new/", views.new, name="new"),
    path("<int:id>/edit", views.edit, name="edit"),
    path("<int:id>/comments", comment_views.create, name="create_comment"),
    path("<int:id>", views.detail, name="detail"),
    path("", views.index, name="index"),
]
