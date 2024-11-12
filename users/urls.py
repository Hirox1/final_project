from django.urls import path
from .views import UserProfileView, UserCreateView, get_verification_code
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', get_verification_code, name='verify'),
]
