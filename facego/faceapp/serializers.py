from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = (
            'content',
            'owner',
            'created_date_time',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = (
            'user',
            'post',
            'content',
            'created_date_time',
            'no_seen',
        )
