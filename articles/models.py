from django.db import models
from django.contrib.auth.models import User

# 什麼時候需要再建一個model，資料是不是一對多？
# 譬如說留言，因為一個article會有很多留言，或是標籤，一個文章可能有很多標籤
# 只要是多對多的，就至少會有三個表格，舉例：英雄、怪獸、對戰記錄表
# 按讚也是一種多對多，每個人可以被很多人按讚，每個人也可以按很多人讚


# Create your models here.
class Article(models.Model):
    # CharField比較接近SQL的varchar
    title = models.CharField(max_length=200, null=False)
    # 大量的文字用TextField
    # 內文可以空，因為有可能文章還沒寫完
    content = models.TextField(null=True)

    # sqlite 本身沒有boolean的資料型態，所以他自動把我們的False變成0
    is_published = models.BooleanField(default=False, null=False)
    # 增加作者欄位，如果沒有null=True，那不能設定成SET_NULL
    user = models.ForeignKey(
        User,
        default=None,
        null=True,
        on_delete=models.SET_NULL,
    )

    # 這樣寫，跟下面設兩個foreignkey的寫法，會有一樣的結果
    # 因為我們想加自己的欄位，所以要用through透過我的Model
    likers = models.ManyToManyField(
        User, related_name="liked_articles", through="FavoriteArticle"
    )

    # 以下兩個方式都可以找到東西
    # Article.objects.get(pk=1).likers 喜歡該文章的人
    # Users.objects.get(pk=1).articles 喜歡哪些文章

    # 魔術方法，顯示出article name
    def __str__(self):
        return self.title


# 製作喜愛文章
class FavoriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
