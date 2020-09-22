from django.contrib import admin
from .models import *


@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(SubCatagory)
class SubCatagoryAdmin(admin.ModelAdmin):
    list_display = ('catogory_name',)
    list_filter = ('catogory_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brands', 'add_time')
    list_filter = ('name', 'brands', 'price')


@admin.register(Imageproduct)
class ImageProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Cosmetic)
class CosmeticAdmin(admin.ModelAdmin):
    pass


@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    pass


@admin.register(HomeApplience)
class HomeApplienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Cultural)
class CulturalAdmin(admin.ModelAdmin):
    pass


@admin.register(Digital)
class DigitalAdmin(admin.ModelAdmin):
    pass
