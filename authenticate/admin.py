from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from authenticate.models import CommentUser


class CommentUserInline(admin.StackedInline):
    model = CommentUser
    can_delete = False
    verbose_name_plural = 'Дополнительные поля'


class UserAdmin(UserAdmin):
    inlines = (CommentUserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


