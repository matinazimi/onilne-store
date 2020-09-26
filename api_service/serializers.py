from rest_framework import serializers

from product.models import *
from finance.models import *


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    brands = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'


class CosmeticSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cosmetic
        fields = '__all__'


class HomeAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeApplience
        fields = '__all__'


class ClothingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clothing
        fields = '__all__'


class DigitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Digital
        fields = '__all__'


class SubcategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCatagory
        fields = '__all__'


class BrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class CulturalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cultural
        fields = '__all__'


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Imageproduct
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class SearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    middle_cart = serializers.PrimaryKeyRelatedField(queryset=Middle_cart.objects.all(), many=True)

    class Meta:
        model = Cart
        fields = '__all__'


class MiddleCartSerializer(serializers.HyperlinkedModelSerializer):
    cart = serializers.StringRelatedField()
    class Meta:
        model = Middle_cart
        fields = '__all__'


class BuyingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Middle_cart
        fields = '__all__'


class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = '__all__'

