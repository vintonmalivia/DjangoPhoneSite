from django.contrib import admin
from django.utils.safestring import mark_safe

from phones.models import *


# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'contents')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'brand', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('get_html_photo', 'time_create', 'time_update')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src=\'{object.photo.url}\' width=50>')

    get_html_photo.short_description = 'Миниатюра'


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Brand, BrandAdmin)

admin.site.site_title = 'Админ-панель сайта о телефонах'
admin.site.site_header = 'Админ-панель сайта о телефонах'
