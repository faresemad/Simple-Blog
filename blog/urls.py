from django.urls import path

from blog.views import post_list

urlpatterns = [
    path("", post_list, name="post_list"),
]
