from .models import AppUser
from rest_framework import viewsets
from .models import BlogPost
from .serializers import UserSerializer, BlogPostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

