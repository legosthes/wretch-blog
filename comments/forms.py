from django.forms import ModelForm, Textarea
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        # 根據我在model設定的Article
        model = Comment
        fields = ["content"]
        labels = {"content": "Comment"}
        # 在這裡客製化表單的樣式
        widgets = {
            "content": Textarea(attrs={"class": "textarea w-full", "rows": 1}),
        }
