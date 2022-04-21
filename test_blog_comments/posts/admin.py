from django.contrib import admin
from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'text',
        'pub_date',
    )
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'text',
        'post',
        'parent',
    )
    empty_value_display = '-пусто-'


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
