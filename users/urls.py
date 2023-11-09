from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from users.views import UserRegister


urlpatterns = [
    path('api/register/', UserRegister.as_view()),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view())

]