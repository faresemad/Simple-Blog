from django.urls import path

from blog.views import PostDetailView, PostListView

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>",
        PostDetailView.as_view(),
        name="post_detail",
    ),
]
