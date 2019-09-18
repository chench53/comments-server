from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, UpvoteList

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)
# router.register(r'upvotes', UpvoteList.as_view())

urlpatterns = [
    path('api/customers/1/', include(router.urls), name='comment'),
    path('api/customers/1/upvotes', UpvoteList.as_view(), name='upvotes'),
]
