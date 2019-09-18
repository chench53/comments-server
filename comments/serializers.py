from rest_framework import serializers

from .models import Creator, Comment, Upvote

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('fullname', 'profile_picture_url')

class CommentSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(source='creator', read_only=True)
    profile_picture_url = serializers.URLField(source='creator', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'creator',
            'fullname',
            'profile_picture_url',
            'created',
            'modified',
            'content',
            'parent',
            'upvote_count'
        )

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = ('creator', 'comment')
