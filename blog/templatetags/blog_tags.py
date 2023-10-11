from django import template

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
