from django.contrib.auth import get_user_model
from posts.models import Comment, Post
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

User = get_user_model()


class FilterCommentListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    comments = serializers.SerializerMethodField(
        method_name='get_comments',
        read_only=True
    )

    class Meta:
        fields = (
            'author',
            'text',
            'pub_date',
            'comments'
        )
        model = Post

    def get_comments(self, obj):
        queryset = obj.comments.all().select_related(
            'author',
            'parent',
        )
        return CommentSerializer(queryset, many=True).data


class CommentChildrenSerializer(serializers.Serializer):

    def to_representation(self, value):
        return CommentSerializer(value, context=self.context).data


class CommentSerializer(serializers.ModelSerializer):
    children = CommentChildrenSerializer(many=True, read_only=True)
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(),
        required=False,
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        fields = (
            'id',
            'author',
            'text',
            'parent',
            'children'
        )
        model = Comment

    def create(self, validated_data):
        if 'parent' not in validated_data:
            return super().create(validated_data)
        return super().create(validated_data)
