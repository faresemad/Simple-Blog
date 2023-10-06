from django.urls import path

from blog.views import PostDetailView, PostListView, CommentCreateView

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
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
]
