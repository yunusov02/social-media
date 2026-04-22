from django.contrib import admin

from .models import Hashtags


@admin.register(Hashtags)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    ordering = ['name']



# admin.site.register(Hashtags, HashtagAdmin)


