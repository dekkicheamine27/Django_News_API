from rest_framework import routers
from news_proxy.views import NewsArticleViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsArticleViewSet)
urlpatterns =  router.urls 