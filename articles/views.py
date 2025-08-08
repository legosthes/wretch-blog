from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib import messages
from .forms import ArticleForm


# Create your views here.
def index(request):
    # 如果是post，那就寫入資料表
    if request.method == "POST":
        # 用forms之後就可以省去以下的那些欄位
        # 他會到你的form的檔案中抓設定好的欄位
        form = ArticleForm(request.POST)
        form.save()

        # # 引號裡的是在html設定的name，如果沒有name，就會抓不到
        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # is_published = request.POST.get("is_published") == "on"
        # # 斜線的title, content是在model時定義的
        # # 寫入table
        # Article.objects.create(title=title, content=content, is_published=is_published)
        # 加一個成功訊息

        messages.success(request, "Article created successfully.")
        return redirect("articles:index")
    else:
        # order by 可以排序，-id是後面的id排在前面，讓新的文章在前面
        # 如果不知道要寫什麼，可以寫all，但如果可以接其他東西像是order_by，那就不用寫all
        # 這裡的filter是資料庫的where的意思
        articles = Article.objects.order_by("-id")
        # articles的key是我在html要讀到的
        return render(request, "articles/index.html", {"articles": articles})


def new(request):
    return render(request, "articles/new.html")


# 在urls如果帶id，在這裡需要再帶一個id的參數
def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    # _method 是在HTML檔裡 name 設定的
    # 先判斷是不是request.POST
    if request.method == "POST":
        if request.POST["_method"] == "patch":
            article.title = request.POST.get("title")
            article.content = request.POST.get("content")
            # 如果request.POST是on，那就會是True
            article.is_published = request.POST.get("is_published") == "on"
            article.save()
            messages.success(request, "Article saved successfully.")
            return redirect("articles:detail", article.id)
        if request.POST["_method"] == "delete":
            article.delete()
            return redirect("articles:index")
    else:
        return render(request, "articles/detail.html", {"article": article})


# 增加編輯
def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, "articles/edit.html", {"article": article})
