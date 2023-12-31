from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from .models import BlogCategory, Post, Comment
from apps.core.models import Tag


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['name', 'url']


class CreateCategoryNodeSerializer(HyperlinkedModelSerializer):

    parent = serializers.IntegerField(required=False)

    def create(self, validated_data):
        parent = validated_data.pop('parent', None)

        if parent is None:
            instance = BlogCategory.add_root(**validated_data)
        else:
            parent_node = get_object_or_404(BlogCategory, pk=parent)
            instance = parent_node.add_child(**validated_data)
        return instance

    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'description', 'is_active', 'url', 'parent']


class CategoryTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        return CategoryTreeSerializer(obj.get_children(), many=True).data

    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'description', 'is_active', 'children']


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'url']


# TaggitSerializer
class PostSerializer(HyperlinkedModelSerializer):
    category = CategorySerializer(many=False)
    # tags = TagSerializer(many=True)
    # tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ['title', 'slug', 'created_at',
                  'updated_at', 'category', 'url']
