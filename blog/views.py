# from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post

# Create your views here.


def post_list(request):
    posts = Post.published.all()
    # render it with HttpResponse without template
    output = ", ".join([str(post) for post in posts])
    return HttpResponse(output)


def post_detail(request, year, month, day, post):
    post = Post.published.get(
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return HttpResponse(post)
