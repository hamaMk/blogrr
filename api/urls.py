from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', views.SearchView.as_view(), name='search-results'),
]
