from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    #author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'likes_count', 'comments_count', 'comments', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'likes_count', 'comments_count', 'comments', 'created_at', 'updated_at']