from products.permissions import IsProductOwner, IsSeller
from products.serializers import GetProductSerializer, ProductSerializer
from core.mixins import SerializerByMethodMixin
from rest_framework import generics, authentication
from products.models import Product


class ProductView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsSeller]

    queryset = Product.objects.all()
    serializer_map = {
        "POST": ProductSerializer, 
        "GET": GetProductSerializer
        }

    def perform_create(self, serializer):
        return serializer.save(account_id=self.request.user.id)


class ProductIdView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsProductOwner]
    lookup_field = "product_uuid"
    queryset = Product.objects.all()
    serializer_map = {
        "PATCH": ProductSerializer, 
        "GET": GetProductSerializer
        }
