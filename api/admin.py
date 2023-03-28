from django.contrib import admin
from django.db import models
from .models import BlogPost, Tag, Image
from tinymce.widgets import TinyMCE


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'last_edited', 'pub_date', 'published', 'owner')
    list_filter = ('published',)
    exclude = ('owner', 'pub_date')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.added_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('img_thumbnail', 'title', 'caption')
    readonly_fields = ['img_thumbnail']



