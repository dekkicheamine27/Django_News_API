from rest_framework.viewsets import  GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from .models import NewsArticle
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import NewsArticleSerializer
from rest_framework import filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class NewsArticleViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):

    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'source']
    search_fields = ['title', 'description', 'category', 'source', 'content' ]

    # Cache the list method
    @method_decorator(cache_page(60*2))  # Caches page for 2 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # Cache the retrieve method
    @method_decorator(cache_page(60*5))  # Caches page for 5 minutes
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
