import logging

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UpvoteForm, DownvoteForm
from .models import Comment, Upvote
from .serializers import CommentSerializer, UpvoteSerializer

# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().select_related('creator')
    serializer_class = CommentSerializer

class UpvoteViewSet(viewsets.ModelViewSet):
    queryset = Upvote.objects.all()
    serializer_class = UpvoteSerializer

class UpvoteList(APIView):
    queryset = Upvote.objects.all()
    serializer_class = UpvoteSerializer

    def post(self, request):
        form = UpvoteForm(request.POST)
        if form.is_valid():
            Upvote.objects.get_or_create(**form.cleaned_data)

        return Response({})

    def get(self, request):
        queryset = Upvote.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class DownvoteList(APIView):
    queryset = Upvote.objects.all()

    def post(self, request):
        form = DownvoteForm(request.POST)
        if form.is_valid():
            Upvote.objects.filter(**form.cleaned_data).delete()
        return Response({})
