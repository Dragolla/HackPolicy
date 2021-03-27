from django.shortcuts import render
from sectionone.models import Post
from sectionone.serializers import PostSerializer
class UserList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
