from .models import AppUser
from rest_framework import viewsets
from .models import BlogPost, Image
from .serializers import UserSerializer, BlogPostSerializer, ImageSerializer
from rest_framework import generics
from rest_framework_roles.granting import is_self
from rest_framework_roles.roles import is_anon


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

    view_permissions = {
        'create': {'admin': True, 'is_author': True},  # only admins and authors are allowed to create posts
        'list': {'is_reader': True, 'anon': is_anon},
        'retrieve': {'is_reader': True, 'anon': is_anon},
        'update': {'admin': True},
    }


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class SearchView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        query = self.request.GET.get('query')
        if not query:
            query = ''
        order = '-pub_date'
        return BlogPost.objects.filter(title__icontains=query).order_by(order)
