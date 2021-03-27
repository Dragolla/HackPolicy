from rest_framework import serializers
from sectionone.models import Post
class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ['post_title', 'post_details']