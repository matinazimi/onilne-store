from django.contrib import admin
from .models import Profile, Address, Phones


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('gender',)
    list_filter = ('gender',)


@admin.register(Address)
class AddresAdmin(admin.ModelAdmin):
    pass


@admin.register(Phones)
class PhoneAdmin(admin.ModelAdmin):
    pass
