from django.contrib import admin
from gallery.models import Photograph

class ListPhotographs(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'active')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ['title', 'category', 'active']
    list_per_page = 20
    list_editable = ('active',)

admin.site.register(Photograph, ListPhotographs)
