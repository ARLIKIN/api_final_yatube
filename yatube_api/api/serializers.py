from rest_framework import serializers

from posts.models import Post, Group, Comment, Follow


class AuthorMixin(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', required=False)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', required=False)
    following = serializers.CharField(source='following.username')

    class Meta:
        model = Follow
        fields = ('user', 'following',)
        read_only_fields = ('user',)


class PostSerializer(AuthorMixin):

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        read_only_fields = ('author',)


class CommentSerializer(AuthorMixin):

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
