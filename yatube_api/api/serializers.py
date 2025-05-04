from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post


class BaseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(BaseSerializer):

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')


class CommentSerializer(BaseSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class FollowSerializer(BaseSerializer):

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')
        read_only_fields = ('user',)
