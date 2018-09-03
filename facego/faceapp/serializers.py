from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = (
            'id',
            'content',
            'owner',
            'created_date_time',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = (
            'id',
            'user',
            'post',
            'created_date_time',
            'no_seen',
            'content',
        )

