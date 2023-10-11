from django.urls import path

from blog.views import CommentCreateView, PostDetailView, PostListView

from .feeds import LatestPostsFeed

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("tag/<slug:tag_slug>", PostListView.as_view(), name="post_list_by_tag"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>",
        PostDetailView.as_view(),
        name="post_detail",
    ),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/comment",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
    path("feed/", LatestPostsFeed(), name="post_feed"),
]
