from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


from posts.models import Posts
from posts.serializers import PostSerializer
from posts.permissions import ManageOwnPosts


class PostManagement(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class SinglePostManagement(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated & ManageOwnPosts]
    serializer_class = PostSerializer
    
    def get_object(self):
        print(self.request.user, self.request.GET.get('post_id'))
        queryset = Posts.objects.get(id=self.kwargs['post_id'])
        return queryset