from django.urls import path
from . import views

app_name = "comments"

# 刪除的話我不需要那麼多資訊，譬如：articles/3/comments/2
# 因為我每個comment都有自己的id，其實只需要id就好了
urlpatterns = [
    path("<int:id>", views.delete, name="delete"),
]
