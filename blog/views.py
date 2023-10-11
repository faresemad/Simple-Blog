from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from taggit.models import Tag

from blog.models import Post

from .forms import CommentForm

# Create your views here.


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3

    def get(self, request, tag_slug=None):
        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            self.queryset = self.queryset.filter(tags__in=[tag])
        return HttpResponse(self.queryset)


class PostDetailView(DetailView):
    def get(self, request, year, month, day, post):
        post = Post.published.get(
            slug=post,
            publish__year=year,
            publish__month=month,
            publish__day=day,
        )
        post_tags_ids = post.tags.values_list("id", flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(
            id=post.id
        )
        similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
            "-same_tags", "-publish"
        )[:4]
        return HttpResponse({"post": post, "similar_posts": similar_posts})


class CommentCreateView(DetailView):
    def get(self, request, year, month, day, post):
        post = Post.published.get(
            slug=post,
            publish__year=year,
            publish__month=month,
            publish__day=day,
        )
        form = CommentForm()
        return HttpResponse(form)

    def post(self, request, year, month, day, post):
        post = Post.published.get(
            slug=post,
            publish__year=year,
            publish__month=month,
            publish__day=day,
        )
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return HttpResponse("Comment Added")
        else:
            return HttpResponse("Comment Not Added")
