from django.urls import path

# views 差不多是前端的部分，html, css, javascript
# 用資料夾創立模組
from . import views


app_name = "pages"
# urlpatterns的名字是固定的
# 幫每個路徑取名字，這樣以後如果有天需要改路徑，就只要改urls.py檔案裡的就好了
# 然後html的連結使用name的標籤
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
