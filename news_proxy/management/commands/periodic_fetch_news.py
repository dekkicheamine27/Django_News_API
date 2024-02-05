# myapp/management/commands/my_periodic_command.py
from django.core.management.base import BaseCommand
import time
from .fetch_news import fetch_news 

class Command(BaseCommand):
    help = 'Periodically fetch news'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting periodic task execution...'))
        
        while True:
            self.stdout.write(self.style.SUCCESS('Starting to fetch news...'))
            fetch_news()  
            self.stdout.write(self.style.SUCCESS('Successfully updated news articles, sleep for 1 hour...'))
            time.sleep(3600)  # Sleep for 1 hour; adjust as needed
