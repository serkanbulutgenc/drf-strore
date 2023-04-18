from rest_framework import serializers
from store.apps.product.models import Product, Category, Brand
from django.utils.text import slugify


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name", "slug"]
        read_only_fields = ["created_at", "updated_at"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
        read_only_fields = ["created_at", "updated_at"]


class ProductSerializer(serializers.ModelSerializer):
    original_price = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
        min_value=float(0),
        max_value=float(9999.99),
        coerce_to_string=False,
    )
    sale_price = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
        min_value=float(0),
        max_value=float(9999.99),
        coerce_to_string=False,
    )
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "title",
            "slug",
            "category",
            "brand",
            "description",
            "qty",
            "original_price",
            "discount_rate",
            "sale_price",
            "is_active",
        ]
        # exclude = ["id"]
        read_only_fields = [
            "categories",
            "created_at",
            "updated_at",
            "slug",
            "discount_rate",
        ]

    def create(self, validated_data):
        validated_data.update({"slug": slugify(validated_data["title"])})
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data["title"]
        instance.slug = slugify(validated_data["title"])
        instance.description = validated_data["description"]
        instance.qty = validated_data["qty"]
        instance.original_price = validated_data["original_price"]
        instance.sale_price = validated_data["sale_price"]
        instance.is_active = validated_data["is_active"]
        instance.save()
        return instance


"""
class ProductSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField(allow_unicode=True, read_only=True)
    description = serializers.CharField()
    qty = serializers.IntegerField()
    original_price = serializers.DecimalField(
        max_digits=6, decimal_places=2, max_value=9999.99, min_value=0
    )
    sale_price = serializers.DecimalField(
        max_digits=6, decimal_places=2, max_value=9999.99, min_value=0
    )
    discount_rate = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    # def validate(self, attrs):
    #     return super().validate(attrs)

    def validate_qty(self, value):
        print(value)
        if value > 100:
            raise serializers.ValidationError("qty must not be greater than 100")
        return value

    def create(self, validated_data):
        validated_data.update({"slug": slugify(validated_data["title"])})
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data["title"]
        instance.slug = slugify(validated_data["title"])
        instance.description = validated_data["description"]
        instance.qty = validated_data["qty"]
        instance.original_price = validated_data["original_price"]
        instance.sale_price = validated_data["sale_price"]
        instance.is_active = validated_data["is_active"]
        instance.save()
        return instance
"""
