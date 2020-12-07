from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=80,
                            verbose_name='Наименование товара')
    description = models.TextField(max_length=240,
                                   verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                blank=True, null=True,
                                default=Decimal("0.00"),
                                verbose_name='Цена')
    categories = models.ManyToManyField('ProductCategory',
                                        blank=True, null=True,
                                        related_name='products', verbose_name='Категория')

    class Meta:
        verbose_name = ' Товар '
        verbose_name_plural = ' Товары '

    def __str__(self):
        return f'{self.name}'

    @property
    def rating(self):
        rating = 0
        rating_values = Review.objects.filter(product=self.pk)
        num_votes = rating_values.count()
        if num_votes != 0:
            for element in rating_values:
                rating += element.value
            rating = rating / num_votes
        return round(rating, 1)


class ProductCategory(MPTTModel):
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=35,
                            verbose_name='Категория')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children', verbose_name="Родительская категория")

    def __str__(self):
        return f'{self.name}'

    class MPTTMeta:
        order_insertion_by = ['name']


class Review(models.Model):
    text = models.TextField(max_length=320,
                            blank=True, null=True,
                            verbose_name='Отзыв')
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    value = models.IntegerField(choices=RATING_CHOICES,
                                verbose_name='Оценка',
                                default=5)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                               verbose_name='Автор')
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                verbose_name='Товар', related_name='review',
                                blank=True, null=True)

    class Meta:
        verbose_name = ' Отзыв '
        verbose_name_plural = ' Отзывы '

    def __str__(self):
        return f'{self.text}'


class Basket(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE,
                                verbose_name='Корзина пользователя')

    class Meta:
        verbose_name = ' Корзина '
        verbose_name_plural = ' Корзины '

    def __str__(self):
        return f'{self.user}'


class ProductInBasket(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                blank=True, null=True,
                                verbose_name='Товар')
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE,
                               blank=True, null=True,
                               verbose_name='Корзина')

    product_quantity = models.IntegerField(default=1,
                                           verbose_name='Количество')

    class Meta:
        verbose_name = ' Товар в корзине '
        verbose_name_plural = ' Товары в корзине '

    def __str__(self):
        return f'{self.product.name}'
