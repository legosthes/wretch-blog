from django.db import models

# Create your models here.
class Article(models.Model):
    # CharField比較接近SQL的varchar
    title = models.CharField(max_length=200,null=False)
    # 大量的文字用TextField
    # 內文可以空，因為有可能文章還沒寫完
    content = models.TextField(null=True)

    # sqlite 本身沒有boolean的資料型態，所以他自動把我們的False變成0
    is_published = models.BooleanField(default=False,null=False)

    # 魔術方法，顯示出article name
    def __str__(self):
        return self.title