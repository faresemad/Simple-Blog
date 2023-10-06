from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from blog.models import Comment, Post

from .forms import CommentForm

# Create your views here.


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3

    def get(self, request):
        return HttpResponse(self.queryset)


class PostDetailView(DetailView):
    def get(self, request, year, month, day, post):
        post = Post.published.get(
            slug=post,
            publish__year=year,
            publish__month=month,
            publish__day=day,
        )
        return HttpResponse(post)


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
