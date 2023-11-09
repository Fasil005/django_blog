from rest_framework import permissions


from posts.models import Posts


class ManageOwnPosts(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        post = Posts.objects.get(id=view.kwargs['post_id'])

        if not(post.user == request.user):
            return True
        else:
            return False