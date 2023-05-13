from django.contrib import admin
from .models import NewsTag, News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsTag)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class NewsAdmin(admin.ModelAdmin):
    pass


