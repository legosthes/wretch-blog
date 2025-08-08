from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        # 根據我在model設定的Article
        model = Article
        fields = ["title", "content", "is_published"]
        # 客製化form上面的標題
        labels = {"title": "Title", "content": "Content", "is_published": "Publish?"}
        # 在這裡客製化表單的樣式
        widgets = {
            "title": TextInput(attrs={"class": "input w-full"}),
            "content": Textarea(attrs={"class": "textarea w-full", "rows": 15}),
            "is_published": CheckboxInput(attrs={"class": "checkbox checkbox-accent"}),
        }
