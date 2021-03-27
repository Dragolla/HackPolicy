from django.shortcuts import render
from sectionone.models import Post
from rest_framework import generics
from rest_framework.views import APIView
from sectionone.serializers import PostSerializer
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
class PostDetail(generics.RetrieveUpdateView):
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
