from django.contrib import admin
from .models import GoodsCategory, SobunTag, SobunPost, Sobun, SobunRate


# Register your models here.

@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(SobunTag)
class SobunTagAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(SobunPost)
class SobunPostAdmin(admin.ModelAdmin):
    fields = ['title', 'user', 'description', 'picture', 'place', 'product', 'sobun_price', 'sobun_unit', 'schedule', 'category',  'tags', 'is_deleted']


@admin.register(Sobun)
class SobunAdmin(admin.ModelAdmin):
    fields = ['post', 'user', 'time', 'whether']


@admin.register(SobunRate)
class SobunRateAdmin(admin.ModelAdmin):
    fields = ['user_from', 'user_to', 'sobun', 'type', 'detail']
