from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse
from .forms import CommentForm
from articles.models import Article
from django.contrib import messages
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Comment
from datetime import datetime


# Create your views here.
# 在函數前加裝飾器，就不用寫request.method=="POST"
# 在執行function之前，會先執行require_POST


@require_POST
@login_required
def create(request, id):
    article = get_object_or_404(Article, pk=id)
    form = CommentForm(request.POST)
    # 先暫存，然後把文章掛給他之後，再把它存起來，因為目前的form沒有收article id
    comment = form.save(commit=False)
    # 把文章掛給它
    comment.article = article
    comment.user = request.user
    comment.save()
    # 把要save的comment，帶進去，這裡算是一種前端的演戲，如果沒有這個變數，我要重新整理才會出現
    return render(request, "comments/comment.html", {"comment": comment})

    # messages.success(request, "Comment added.")
    # return redirect("articles:detail", article.id)


# 以下這句取代的意思就是if request.method=="DELETE"
@require_http_methods(["DELETE"])
@login_required
def delete(request, id):
    # 改用htmx後
    comment = get_object_or_404(Comment, pk=id, user=request.user)
    # 軟刪除，只篩選有刪除日期的
    # 其實可以把以下的，寫在model裡
    # 這樣就可以用這樣的方式叫出來comment.delete()，會看起來比較乾淨
    # comment.deleted_at = datetime.now()
    # comment.save()
    comment.delete()
    # messages.warning(request, "Comment deleted.")
    return HttpResponse("")
    # 改成htmx後，他就會把button那一區redirect為以下，所以我需要return以上才讓他變成空值
    # return redirect("articles:detail", comment.article_id)
