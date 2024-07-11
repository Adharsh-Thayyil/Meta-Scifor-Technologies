import requests
from django.core.management.base import BaseCommand
from myapp.models import Post

class Command(BaseCommand):
    help = 'fetch post from json placeholder and populate the database'
    def handle(self, *args, **kwargs):
        response = requests.get('https://jsonplaceholder.typicode.com/')
        posts = response.json()

        for post_data in posts:
            Post.objects.update_or_create(
                id = post_data['id'],
                defaults={
                    'user_id': post_data['userId'],
                    'title' : post_data['title'],
                    'body': post_data['body'],
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully Populated the Database with Posts'))