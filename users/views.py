from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django_redis import get_redis_connection
from rest_framework.decorators import api_view


# View for user CRUD
class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(CustomUser, id=self.request.user.id)


# User Registration View
class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# Generate 4-digit Redis Code
@api_view(['GET'])
def get_verification_code(request):
    if request.user.is_authenticated:
        redis_conn = get_redis_connection("default")
        code = random.randint(1000, 9999)
        redis_conn.setex(f"verify_code:{request.user.id}", 3600, code)
        return Response({'code': code})
    return Response(status=status.HTTP_401_UNAUTHORIZED)
