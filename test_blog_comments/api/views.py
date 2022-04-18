from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from posts.models import Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import CheckingUserIsAuthor
from .serializers import CommentSerializer, PostSerializer

User = get_user_model


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (CheckingUserIsAuthor, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (CheckingUserIsAuthor, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(
            post=post,
            author=self.request.user,
        )
