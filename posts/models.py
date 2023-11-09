from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, related_name="user_posts", on_delete=models.CASCADE)

    class Meta:

        ordering = ('-created_at',)

    def __str__(self, ):
        return  f"{self.title}"