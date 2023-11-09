from rest_framework import generics


from django.contrib.auth.models import User


from users.serializers import UserCreateSerializer


class UserRegister(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

