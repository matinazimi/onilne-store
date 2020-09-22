from django.contrib import admin
from .models import Cart, Middle_cart, Finance


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ('user',)
    fields = ('id', 'cart', 'user')
    readonly_fields = ('id',)
    list_filter = ('user',)


@admin.register(Cart)
class CartAmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'status', 'totalprices', 'TotalPro')
    fields = ('user', 'status', 'totalprices', 'TotalPro')
    readonly_fields = ('id', 'totalprices', 'TotalPro')
    list_filter = ('user', 'date', 'status')


@admin.register(Middle_cart)
class MiddleAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'purchase_number', 'price')
    readonly_fields = ('price',)
    list_filter = ('product', 'cart', 'purchase_number',)
