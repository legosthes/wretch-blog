from django.urls import path, include
from django.contrib import admin

# views 差不多是前端的部分，html, css, javascript
# 用資料夾創立模組
# from pages.views import home, about

urlpatterns = [
    # 只要到首頁，就會去找pages.urls的檔案
    path("", include("pages.urls")),
    path("articles/", include("articles.urls")),
    path("comments/", include("comments.urls")),
    path("admin/", admin.site.urls),
]
