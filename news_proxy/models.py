from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=100)
    published_at = models.DateTimeField()
    url = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500, null=True)
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
