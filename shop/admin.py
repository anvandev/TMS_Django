from django.contrib import admin
from .models import Product, ProductCategory, Review, Basket, ProductInBasket
from mptt.admin import MPTTModelAdmin

admin.site.register(Product)


class CategoryMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ('name', 'parent', 'tree_id', 'level')
    fields = ('name', 'parent')


admin.site.register(ProductCategory, CategoryMPTTModelAdmin)
admin.site.register(Review)
admin.site.register(Basket)
admin.site.register(ProductInBasket)
