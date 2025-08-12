from django.urls import path, include
from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls

# views 差不多是前端的部分，html, css, javascript
# 用資料夾創立模組
# from pages.views import home, about

urlpatterns = [
    # 只要到首頁，就會去找pages.urls的檔案
    path("", include("pages.urls")),
    path("articles/", include("articles.urls")),
    path("comments/", include("comments.urls")),
    path("users/", include("users.urls")),
    path("sessions/", include("sessions.urls")),
    path("admin/", admin.site.urls),
] + debug_toolbar_urls()
