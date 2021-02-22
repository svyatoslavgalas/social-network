from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from post.models import Post
from .serializers import (PostSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # HTTP GET /api/post/<int:id>/like-post/
    @action(detail=True, url_path='like-post', methods=['post'])
    def like_post(self, request, pk):
        if not request.user.is_authenticated:
            return Response('Пользователь не авторизирован', status=401)

        post = Post.objects.get(pk=pk)
        msg = 'Вы поставили лайк публикации:'

        if request.user in post.likes.all():
            msg = 'Вы отменили лайк публикации'
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return Response('{} {}'.format(msg, post.name))

