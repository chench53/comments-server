from rest_framework import serializers

from .models import Creator, Comment, Upvote

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('fullname', 'profile_picture_url')

class CommentSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(source='creator', read_only=True)
    profile_picture_url = serializers.URLField(source='creator', read_only=True)

    created_by_current_user = serializers.SerializerMethodField()
    user_has_upvoted = serializers.SerializerMethodField()

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
            'upvote_count',
            'created_by_current_user',
            'user_has_upvoted',
        )
    
    def get_created_by_current_user(self, obj):
        try:
            current_user = self.context['request'].query_params['current_user']
            created_by_current_user = str(obj.creator.id) == str(current_user)
        except (AttributeError, KeyError):
            created_by_current_user = False
        return created_by_current_user

    def get_user_has_upvoted(self, obj):
        try:
            current_user = self.context['request'].query_params['current_user']
            user_has_upvoted = bool(Upvote.objects.get(creator=current_user, comment=obj.id))
        except (KeyError, Upvote.DoesNotExist):
            user_has_upvoted = False
        return user_has_upvoted

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = ('creator', 'comment')
