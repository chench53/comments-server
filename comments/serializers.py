from rest_framework import serializers

from .models import Creator, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('created', 'modified', 'content')
