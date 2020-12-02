from django.db import models
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
