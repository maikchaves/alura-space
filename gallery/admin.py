from django.contrib import admin
from gallery.models import Photograph

class ListPhotographs(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'user', 'active')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description', 'user')
    list_filter = ['title', 'category', 'active', 'user']
    list_per_page = 20
    list_editable = ('active',)

admin.site.register(Photograph, ListPhotographs)
