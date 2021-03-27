from rest_framework import serializers
from sectionone.models import Post
class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ['post_title', 'post_details']
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)   
