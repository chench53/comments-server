from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, UpvoteViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'upvotes', UpvoteViewSet)

urlpatterns = [
    path('api/customers/1/', include(router.urls), name='comments'),
    path('api/customers/1/', include(router.urls), name='upvotes'),
]
