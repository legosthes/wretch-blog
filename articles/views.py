from django.shortcuts import render, redirect
from django.http import HttpResponse
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
       
        return redirect("articles:index")
    else:
        # order by 可以排序，-id是後面的id排在前面，讓新的文章在前面
        # 如果不知道要寫什麼，可以寫all，但如果可以接其他東西像是order_by，那就不用寫all
        articles = Article.objects.all().order_by("-id")
        # articles的key是我在html要讀到的
        return render(request, "articles/index.html",
        {"articles":articles})

def new(request):
    return render(request,"articles/new.html")

# 在urls如果帶id，在這裡需要再帶一個id的參數
def detail(request, id):
    return render(request,"articles/detail.html",{"id":id})