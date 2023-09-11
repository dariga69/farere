from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from apps.users.serializers import UserSerializer, UserCreateSerializer


class RegisterAPIView(APIView):

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    authentication_classes = (JWTAuthentication, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

