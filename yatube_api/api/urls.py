from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(
    'posts',
    PostViewSet,
    basename='posts',
)
router_v1.register(
    'groups',
    GroupViewSet,
    basename='groups',
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router_v1.register(
    'follow',
    FollowViewSet,
    basename='follow',
)

urlpatterns_v1 = [
    path('', include('djoser.urls.jwt')),
    path('', include(router_v1.urls)),
]

urlpatterns = [
    path('v1/', include(urlpatterns_v1)),
]
