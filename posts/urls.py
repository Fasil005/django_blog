from django.urls import path


from posts.views import PostManagement, SinglePostManagement


urlpatterns = [
    path('api/posts/', PostManagement.as_view()),
    path('api/posts/<post_id>/', SinglePostManagement.as_view()),
]