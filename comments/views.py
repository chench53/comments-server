from django.shortcuts import render
from rest_framework import viewsets

from .models import Comment
from .serializers import CommentSerializer

# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all().select_related('creator')
    serializer_class = CommentSerializer
