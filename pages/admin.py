from django.contrib import admin
from .models import Proje, Category, FormModel
# Register your models here.


@admin.register(Proje)
class ProjeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields={'slug':('title',)}
    list_filter=("category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields={'slug':('name',)}


@admin.register(FormModel)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name',)