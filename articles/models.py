from django.db import models

# Create your models here.
class Article(models.Model):
    # CharField比較接近SQL的varchar
    title = models.CharField(max_length=200,null=False)
    # 大量的文字用TextField
    # 內文可以空，因為有可能文章還沒寫完
    content = models.TextField(null=True)