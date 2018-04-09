from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.User', verbose_name="Автор")
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Краткое описание")
    text = models.TextField("Текст статьи")
    created_date = models.DateField("Создано", default=timezone.now)
    published_date = models.DateField("Опубликовано", blank=True, null=True)
    category = models.ForeignKey('Category', verbose_name="Категория")
    status = models.BooleanField("Статус", default=False)
    slug = models.SlugField("URL поста")
    image = models.ImageField(blank=False, null=True)

    class Meta:
        verbose_name = u"пост"
        verbose_name_plural = u"посты"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField("Название категории", max_length=60)
    slug = models.SlugField("URL категории")
    description = models.TextField("Описание категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"категория"
        verbose_name_plural = u"категории"


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name="Пользователь")
    post = models.ForeignKey(Post, verbose_name="Статья")
    text = models.TextField("Текст комментария", max_length=1000)
    created_date = models.DateTimeField("Добавлен", auto_now_add=True)
    moder = models.BooleanField("Модерация", default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = u"комментарий"
        verbose_name_plural = u"комментарии"


# не проверено
# class Image(models.Model):
#     post = models.ForeignKey(Post, verbose_name="Изображение")
#     title = models.TextField("Название изображения", max_length=256)
#     description = models.TextField("Описание изображения", max_length=1000)
#     upload_date = models.DateTimeField("Добавлен", auto_now_add=True)
#     image = models.ImageField(upload_to='images/blog')

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = u"изображение"
#         verbose_name_plural = u"изображения"