from products.models import Product
from accounts.serializers import AccountSerializer
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["is_active"]

    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        data["account"].update({"id": instance.account.id})
        return data

class GetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
