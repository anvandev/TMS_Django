from django.db import models
from django.utils import timezone
from django.db.models import Avg, Count



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                               verbose_name='Автор')
    title = models.CharField(max_length=56,
                             verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name='Дата создания')
    view = models.IntegerField(default=0,
                               verbose_name='Просмотры')
    like = models.IntegerField(default=0,
                               verbose_name='Лайк')
    dislike = models.IntegerField(default=0,
                                  verbose_name='Дислайк')
    draft = models.BooleanField(default=True,
                                verbose_name='Черновик')
    favorites = models.BooleanField(default=False,
                                    verbose_name='Избранное')
    tag = models.ManyToManyField('Tag',
                                 related_name='posts', verbose_name='Тег')
    category = models.ForeignKey('Category', default=1, on_delete=models.CASCADE,
                                 related_name='posts', verbose_name='Категория')
    image = models.ImageField(null=True, blank=True,
                              upload_to="post/images/",
                              verbose_name='Изображение')

    @property
    def rating(self):
        r = Rating.objects.filter(post=self.pk).aggregate(ra=Avg('rating'), num=Count('rating'))
        if not r['ra']:
            r['ra'] = 0
        return {'rating': round(r['ra'], 1), 'number': r['num']}

    class Meta:
        verbose_name = ' Пост '
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             verbose_name='Пост', related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                               verbose_name='Автор')
    text = models.TextField(verbose_name='Новый комментарий')
    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name='Дата создания')

    class Meta:
        verbose_name = ' Комментарий '
        verbose_name_plural = ' Комментарии '

    def __str__(self):
        return f'{self.post}:{self.author}:{self.pk} '


class Rating(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Пост', related_name='ratings')
    rating = models.IntegerField(verbose_name="Рейтинг")

    class Meta:
        verbose_name = ' Рейтинг '
        verbose_name_plural = ' Рейтинг '

    def __str__(self):
        return f'{self.rating}'


class Tag(models.Model):
    tag_name = models.CharField(max_length=24, verbose_name="Тэг")

    class Meta:
        verbose_name = ' Тэг '
        verbose_name_plural = ' Тэги'

    def __str__(self):
        return f'{self.tag_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=24, verbose_name="Категория")

    class Meta:
        verbose_name = ' Категория '
        verbose_name_plural = ' Категории '

    def __str__(self):
        return f'{self.category_name}'
