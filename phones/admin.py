from django.contrib import admin
from phones.models import *


# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'contents')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Brand, BrandAdmin)
