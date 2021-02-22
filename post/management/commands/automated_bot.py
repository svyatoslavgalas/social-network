import os, random
from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from django.db.models import Max

from account.models import User
from post.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_dotenv()
        number_of_users = int(os.getenv('number_of_users'))
        max_posts_per_user = int(os.getenv('max_posts_per_user'))
        max_likes_per_user = int(os.getenv('max_likes_per_user'))
        for i in range(1, number_of_users):
            User.objects.create_user(
                email='user%s@gmail.com' % i,
                password='q1w2e3r4t5',
            )

        users = User.objects.all()

        for user in users:
            for i in range(1, max_posts_per_user):
                post = Post.objects.create(
                    user=user,
                    name='Запись #%s, автор %s',
                    content='Текстовый контент'
                )
                while post.likes_count < max_likes_per_user:
                    max_val_id = User.objects.all().aggregate(max_id=Max('id'))['max_id']
                    pk = random.randint(1, max_val_id)
                    user = User.objects.get(pk=pk)
                    post.likes.add(user)



