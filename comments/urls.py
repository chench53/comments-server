from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/customers/1/', include(router.urls), name='comments'),
]
