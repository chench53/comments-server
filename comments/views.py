import logging

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UpdvateForm
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
        form = UpdvateForm(request.POST)
        # form.update_or_create()
        print(request.POST)
        print(form)
        Upvote.objects.get_or_create(creator=request.POST['creator'], comment=request.POST['comment'])
        return Response({})

    def get(self, request):
        queryset = Upvote.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
