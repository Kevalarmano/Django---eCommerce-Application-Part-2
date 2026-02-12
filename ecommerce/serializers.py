from rest_framework import serializers
from .models import Store, Product, Review


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["id", "owner", "name"]
        read_only_fields = ["id", "owner"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "store", "name", "description", "price", "image"]
        read_only_fields = ["id"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "product", "buyer", "rating", "comment", "created_at"]
        read_only_fields = ["id", "buyer", "created_at"]
