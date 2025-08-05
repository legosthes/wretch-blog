from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 如果是post，那就寫入資料表
    if request.POST:
        # 引號裡的是在html設定的name，如果沒有name，就會抓不到
        title = request.POST['title']
        content = request.POST['content']
        # 斜線的title, content是在model時定義的
        # 寫入table
        Article.objects.create(title=title,content=content)
       
        return redirect("pages:home")
    else:
        return render(request, "articles/index.html")

def new(request):
    return render(request,"articles/new.html")