from django.contrib import admin
from .models import Post, Comment, Tag, Category, Rating

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Rating)
