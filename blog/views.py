from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm
import markdown


# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        category__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    # Pulling out the post we need
    post = Post.objects.get(pk=pk)
    form = CommentForm()

    # Converting the post to markdown
    body_text = post.body_text
    md = markdown.Markdown(extensions=["fenced_code"])
    body_text = md.convert(body_text)

    # Logic for the form
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body_text=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    # Setting context for html doc
    comments = Comment.objects.filter(post=post)
    context = {
        "title": post.title,
        "body_text": body_text,
        "comments": comments,
        "form": CommentForm(),

    }

    return render(request, "blog/details.html", context)
