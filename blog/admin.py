from django.contrib import admin

from blog.models import Comment, Post

# Register your models here.

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "auther", "publish", "status")
    list_filter = ("status", "created_at", "publish", "auther")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("auther",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_at", "active"]
    list_filter = ["active", "created_at", "updated_at"]
    search_fields = ["user", "body"]
