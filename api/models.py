from django.db import models
from users.models import AppUser
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse
import datetime

POST_TITLE_MAX_LENGTH = settings.POST_TITLE_MAX_LENGTH


class UserOwnedModel(models.Model):
    owner = models.ForeignKey(AppUser, on_delete=models.PROTECT, default=None, blank=True, null=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class BlogPost(UserOwnedModel):
    title = models.CharField(max_length=POST_TITLE_MAX_LENGTH)
    short_description = models.CharField(max_length=500)
    content = models.TextField()
    slug = models.SlugField(max_length=POST_TITLE_MAX_LENGTH, editable=False, unique=True)
    tags = models.ManyToManyField(Tag, blank=True)
    featured_image = models.ForeignKey('Image', on_delete=models.PROTECT, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    pub_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('posts', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if self.published:
            self.pub_date = datetime.datetime.now()
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}: {self.pub_date}"


class Image(models.Model):
    title = models.CharField(max_length=50, unique=True)
    caption = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=False, null=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



