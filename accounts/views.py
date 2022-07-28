from accounts.models import Account
from django.contrib.auth import authenticate
from accounts.permissions import IsOwner, IsSuperAdmin
from rest_framework.authtoken.models import Token
from rest_framework import generics, authentication
from accounts.serializers import AccountManagement, AccountSerializer, LoginSerializer
from rest_framework.views import APIView, Response, Request, status

class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountIdView(generics.UpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [IsOwner]
    lookup_field = "user_uuid"

class AccountNewestView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        num = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:num]

class AccountManagementView(generics.UpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsSuperAdmin]
    queryset = Account.objects.all()
    serializer_class = AccountManagement
    lookup_field = "user_uuid"

class LoginView(APIView):
    def post(self, request: Request):
        serialized = LoginSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        user = authenticate(**serialized.data)

        print(user)

        if not user:
            return Response(
                {"detail": "invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"Token": token.key}, status=status.HTTP_200_OK)
