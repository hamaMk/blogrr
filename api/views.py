from .models import AppUser
from rest_framework import viewsets
from .models import BlogPost, Image
from .serializers import UserSerializer, BlogPostSerializer, ImageSerializer
from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


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
