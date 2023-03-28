from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'last_edited', 'pub_date', 'published', 'owner')
    list_filter = ('published', )



