from django.contrib import admin
from .models import User, Customer, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'city', 'state', 'zip', 'country', 'picture')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user",)
