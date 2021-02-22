from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from account.models import User
from post.models import Post

from .utils import (check_email, get_additional_data)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name')

    # HTTP POST /api/user/ - signup user
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        add_info = get_additional_data(email)
        if check_email(email):
            user = User.objects.create_user(
                email=email,
                password=password,
            )
            if add_info:
                user.first_name, user.last_name = add_info
                user.save()
            return user


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('user', 'name', 'pub_date', 'content', 'likes', 'likes_count')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        post = Post.objects.create(
            user=user,
            name=validated_data['name'],
            content=validated_data['content']
        )

        return post

