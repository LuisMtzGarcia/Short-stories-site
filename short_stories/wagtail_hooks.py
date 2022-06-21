from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Story, Genre

class GenreAdmin(ModelAdmin):
    model = Genre
    menu_label = 'Genre'
    menu_icon = 'pilcrow'
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name')
    list_filter = ('name',)
    search_fields = ('name',)

modeladmin_register(GenreAdmin)

class StoryAdmin(ModelAdmin):
    model = Story
    menu_label = 'Story'
    menu_icon = 'pilcrow'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'genre', 'synopsis', 'text',)
    list_filter = ('genre',)
    search_fields = ('title', 'genre')

modeladmin_register(StoryAdmin)