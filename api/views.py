from .models import AppUser
from rest_framework import viewsets
from .models import BlogPost, Image
from .serializers import UserSerializer, BlogPostSerializer, ImageSerializer
from rest_framework import generics
from rest_framework_roles.granting import is_self
from rest_framework_roles.roles import is_anon
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    view_permissions = {
        'create': {'anon': True},  # only anonymous visitors allowed
        'list': {'admin': True},
        'retrieve': {'user': is_self},
        'update': {'user': is_self, 'admin': True},
    }


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['owner', 'published']
    search_fields = ['title', 'short_description']
    ordering_fields = ['creation_date', 'last_edited', 'pub_date']
    ordering = ['-pub_date']
    lookup_field = 'slug'

    view_permissions = {
        'create': {'admin': True, 'is_author': True},  # only admins and authors are allowed to create posts
        'list': {'is_reader': True, 'anon': is_anon},
        'retrieve': {'is_reader': True, 'anon': is_anon},
        'update': {'admin': True},
    }


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
