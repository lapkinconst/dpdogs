from django.db import models
from django.contrib.auth.models import User


class CommentUser(models.Model):
    user = models.OneToOneField(User, unique=True)
    age = models.IntegerField("Возраст")
    description = models.TextField("О себе")
    avatar = models.ImageField(blank=True, default="../blog/static/media/avatar.jpg")

    class Meta:
        verbose_name = u"доп. поле"
        verbose_name_plural = u"доп. поля"
