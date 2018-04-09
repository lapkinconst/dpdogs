from django.contrib import admin
from .models import Post, Category, Comment
# , Image


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_date', 'status', )
    list_display_links = ('title', 'description')
    list_filter = ('title', 'created_date', 'status')
    search_fields = ('id', 'title', 'description')
    prepopulated_fields = {'slug': ('title',), }


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'text', 'created_date', 'moder', )
    list_display_links = ('post', 'text')
    list_filter = ('post__title', 'created_date', 'moder')
    search_fields = ('id', 'post__title', 'text')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', )
    list_display_links = ('title', 'description')
    list_filter = ('title',)
    search_fields = ('id', 'title', 'description')
    prepopulated_fields = {'slug': ('title',), }

# не проверено
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'description',)
#     list_display_links = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.register(Image, ImageAdmin)
