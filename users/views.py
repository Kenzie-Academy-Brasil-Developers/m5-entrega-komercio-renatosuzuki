from rest_framework.views import Request, Response, status, APIView
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from .serializers import LoginSerializer, UserSerializer, UserDisableSerializer, UserUpdateSerializer
from .models import User
from .permissions import OwnAccountPermission, OnlyAdminPermission



class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status.HTTP_200_OK)

        return Response({"detail": "wrong username or password"}, status.HTTP_400_BAD_REQUEST)


class UserListByEntryDateDetailView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        entry_date = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:entry_date]


class UserUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OwnAccountPermission]

    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class UserDisableView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OnlyAdminPermission]

    serializer_class = UserDisableSerializer
    queryset = User.objects.all()