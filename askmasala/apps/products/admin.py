from django.contrib import admin
from .models import Products, Images, Categories

admin.site.register(Categories)

class ProductInstance(admin.TabularInline):
    model = Images

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductInstance]
