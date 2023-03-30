from django.contrib.auth import get_user_model
from .models import BlogPost, Tag, Image
from rest_framework import serializers

AppUser = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = AppUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = AppUser
        fields = ['url', 'email', 'password', 'role']


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['url', 'slug', 'title', 'short_description', 'content', 'owner']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['url', 'name']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'title']
