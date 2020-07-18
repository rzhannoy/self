import json

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Generates a list of all routes and dumps to json file for a web app'

    def handle(self, **options):
        from core.models import Post

        # Static routes
        routes = ['/', '/i/apps']

        for post in Post.objects.all().iterator():
            routes.append(f'/{post.slug}')

        with open(f'{settings.WEB_DIR}/routes.json', 'w') as f:
            json.dump(routes, f)
