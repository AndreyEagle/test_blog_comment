from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, PostViewSet

app_name = 'posts'
app_name = 'api'

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>[^/.]+)/comment',
    CommentViewSet,
    basename='comment'
)


urlpatterns = [
    path('', include(router.urls)),
]
