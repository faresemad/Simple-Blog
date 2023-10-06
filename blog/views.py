from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from blog.models import Post

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
