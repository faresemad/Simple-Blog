import markdown
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


"""
when we use it in template, we can use it like this:
{% load blog_tags %}
{% total_posts %}
"""


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}


"""
when we use it in template, we can use it like this:
{% load blog_tags %}
{% show_latest_posts 3 %}
"""


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count("comments")).order_by(
        "-total_comments"
    )[:count]


"""
when we use it in template, we can use it like this:
{% load blog_tags %}
{% get_most_commented_posts as most_commented_posts %}
{% for post in most_commented_posts %}
    ...
{% endfor %}
"""


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


"""
when we use it in template, we can use it like this:
{% load blog_tags %}
{{ post.body|markdown }}
"""
