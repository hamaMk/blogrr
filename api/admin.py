from django.contrib import admin
from django.db import models
from .models import BlogPost, Tag
from tinymce.widgets import TinyMCE


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'last_edited', 'pub_date', 'published', 'owner')
    list_filter = ('published',)

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )



