from django.core.management.base import BaseCommand
import requests
import pytz
from django.utils import timezone
from datetime import datetime
from news_proxy.models import NewsArticle
from news_dashboard import settings


def fetch_news():
    
    category_list = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    
    
    api_key = settings.NEWSAPI_KEY
    base_url = settings.BASE_URL
    

    params = {
        'language': 'en',
        'apiKey': api_key,
    }


    # fetch new for ech category and store them
    for category in category_list:
        params['category'] = category
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            news_data = response.json()
            for article in news_data['articles']:
                if article['title'] != "[Removed]":
                    published_at_naive = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
                    published_at_aware = timezone.make_aware(published_at_naive, pytz.UTC)
                    NewsArticle.objects.update_or_create(
                        title=article['title'],
                        defaults={
                            'description': article.get('description', 'No description available'),
                            'content': article.get('content', 'No content available'),
                            'url': article['url'],
                            'published_at': published_at_aware,
                            'source': article['source']['name'],
                            'image_url': article.get('urlToImage', ''),
                            'category': category
                        },
                    )
        else:
            print("fetching data is faild")   