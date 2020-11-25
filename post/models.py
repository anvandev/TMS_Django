from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=56, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    view = models.IntegerField(default=0, verbose_name='Просмотры')
    like = models.IntegerField(default=0, verbose_name='Лайк')
    dislike = models.IntegerField(default=0, verbose_name='Дислайк')
    draft = models.BooleanField(default=True, verbose_name='Черновик')
    tag = models.TextField(verbose_name='Тег')
    image = models.ImageField(null=True, blank=True, upload_to="post/images/", verbose_name='Изображение')

    class Meta:
        verbose_name = ' Пост '
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Новый комментарий')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name = ' Комментарий '
        verbose_name_plural = ' Комментарии '

    def __str__(self):
        return f'{self.post}:{self.author}:{self.pk} '
