from rest_framework import serializers
from .models import BlogItems

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogItems
        fields=['id','blog_tittle','blog_description']