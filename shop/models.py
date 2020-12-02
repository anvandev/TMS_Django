from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=80, verbose_name='Наименование товара')
    description = models.TextField(max_length=240, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=Decimal("0.00"),
                                verbose_name='Цена')

    class Meta:
        verbose_name = ' Товар '
        verbose_name_plural = ' Товары '

    def __str__(self):
        return f'{self.name}'


class ProductCategory(MPTTModel):
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=35, verbose_name='Категория')
    parent = TreeForeignKey('self', null=True, blank=True,
                            on_delete=models.CASCADE, related_name='children', verbose_name="Родительская категория")

    def str(self):
        return f'{self.name}'

    class MPTTMeta:
        order_insertion_by = ['name']
