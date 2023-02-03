from django.contrib import admin
from .models import GoodsCategory, SobunTag, SobunPost, Sobun, SobunRate


# Register your models here.

@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    fields = ('id', 'name')


@admin.register(SobunTag)
class SobunTagAdmin(admin.ModelAdmin):
    fields = ('id', 'name')

@admin.register(SobunPost)
class SobunPostAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'user', 'category', 'tags', 'is_deleted', 'updated_at', 'created_at')

@admin.register(Sobun)
class SobunAdmin(admin.ModelAdmin):
    fields = ('id', 'post', 'user', 'time', 'whether', 'updated_at', 'created_at')

@admin.register(SobunRate)
class SobunRateAdmin(admin.ModelAdmin):
    fields = ('id', 'user_from', 'user_to', 'sobun', 'type', 'detail' 'updated_at', 'created_at')