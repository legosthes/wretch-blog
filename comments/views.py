from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CommentForm
from articles.models import Article
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Comment
from datetime import datetime


# Create your views here.
# 在函數前加裝飾器，就不用寫request.method=="POST"
# 在執行function之前，會先執行require_POST


@require_POST
def create(request, id):
    if request.method == "POST":
        article = get_object_or_404(Article, pk=id)
        form = CommentForm(request.POST)
        # 先暫存，然後把文章掛給他之後，再把它存起來，因為目前的form沒有收article id
        comment = form.save(commit=False)
        # 把文章掛給它
        comment.article = article
        comment.save()
        messages.success(request, "Comment added.")
        return redirect("articles:detail", article.id)


def delete(request, id):
    # 改用htmx後
    if request.method == "DELETE":
        comment = get_object_or_404(Comment, pk=id)
        # 軟刪除，只篩選有刪除日期的
        # 其實可以把以下的，寫在model裡
        # 這樣就可以用這樣的方式叫出來comment.delete()，會看起來比較乾淨
        # comment.deleted_at = datetime.now()
        # comment.save()
        comment.delete()
        messages.warning(request, "Comment deleted.")
        return HttpResponse("")
        # return redirect("articles:detail", comment.article_id)
