from django.contrib import admin
from blog.models import Post, Tag, Comment


# class PostInline(admin.TabularInline):
#     model = Post.comments.through
#     raw_id_fields = ('post', 'comment')
#     verbose_name = 'Связь с комментариями'


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes', 'tags', 'author', )
    # inlines = [PostInline, ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text'[:20])
    raw_id_fields = ('post', 'author', )


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
