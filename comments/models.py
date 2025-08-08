from django.db import models
from articles.models import Article
from datetime import datetime


# Create your models here.
class Comment(models.Model):
    content = models.TextField(null=False)
    # 文章FK，on_delete是當你被刪掉的時候，那我要怎麼辦？（參考SQL）
    # CASCADE就是，你刪了，那我的留言也會被刪掉
    # 這樣article的資料表裡也會多一個comment_set
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    # 建立時間
    # auto_now_add 建立的時間寫進去，auto_now 則是現在的時間
    # 寫進資料庫的時間要固定，然後再根據不同時區去顯示
    created_at = models.DateTimeField(auto_now_add=True)
    # soft delete，兩種做法
    # 1
    # is_deleted = models.BooleanField(default=False)
    # 2，可以看出什麼時候被刪掉
    # 加索引 index，不用每個欄位都加，否則寫入會變慢
    # 因為刪除不常刪，所以適合加索引
    deleted_at = models.DateTimeField(null=True, db_index=True)

    def delete(self):
        self.deleted_at = datetime.now()
        self.save()
