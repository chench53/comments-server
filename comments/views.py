from django.shortcuts import render
from rest_framework import viewsets

from .models import Comment, Upvote
from .serializers import CommentSerializer, UpvoteSerializer

# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all().select_related('creator')
    serializer_class = CommentSerializer

class UpvoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Upvote.objects.all()
    serializer_class = UpvoteSerializer
