from django.db.models import Q

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class ProductView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        """
        override this method for can filter on product

        """
        if request.query_params:
            p = request.query_params.items()
            for i, d in p:
                if i == 'category':
                    category = Catagory.objects.get(name=d)
                    product = Product.objects.all().filter(category=category.id)
                    serializer = ProductSerializer(product, many=True)
                    return Response(serializer.data)
                if i == 'subcategory':
                    subcategory = SubCatagory.objects.get(catogory_name=d)
                    product = Product.objects.all().filter(sub_catagory=subcategory.id)
                    serializer = ProductSerializer(product, many=True)
                    return Response(serializer.data)
        else:
            return super().list(self, request, *args, **kwargs)


class ClothingView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer


class CosmeticView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Cosmetic.objects.all()
    serializer_class = CosmeticSerializer


class HomeAppView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = HomeApplience.objects.all()
    serializer_class = HomeAppSerializer


class BrandView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ImageView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Imageproduct.objects.all()
    serializer_class = ImageSerializer


class CommentView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CulturalView(viewsets.ModelViewSet):
    queryset = Cultural.objects.all()
    serializer_class = CulturalSerializer


class DigitalView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Digital.objects.all()
    serializer_class = DigitalSerializer


class CategorylView(viewsets.ReadOnlyModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Catagory.objects.all()
    serializer_class = CategorySerializer


class SubCatView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = SubCatagory.objects.all()
    serializer_class = SubcategorySerializer


class SearchView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """

    serializer_class = SearchSerializer

    def get_queryset(self):
        """
        override this method for can filter on query
        """
        search_text = self.request.query_params.items()
        for i, d in search_text:
            result = Product.objects.filter(
                Q(name__icontains=d) |
                Q(price__icontains=d)
            )
            return result


class CartView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        override this method because if users have not cart this method create for them

        """
        try:
            cart = Cart.objects.all()
            if not Cart.objects.all():
                cart = Cart.objects.create(user_id=request.user.id)
            serializer = ProductSerializer(cart, many=True)
            return Response(serializer.data)
        except:
            return super().list(self, request, *args, **kwargs)


class MiddleCartView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Middle_cart.objects.all()
    serializer_class = BuyingSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


def get_or_createcart(self, request):
    """
    this function return user cart or create

    """
    if not Cart.objects.filter(user_id=request.user.id):
        cart = Cart.objects.create(user_id=request.user.id)
        return cart.id
    else:
        cart = Cart.objects.get(user_id=request.user.id)
        return cart.id


def createmiddlecart(self, request, product_id, numbers):
    """
    this function create or update middle cart

    """
    cartid = get_or_createcart(self, request)
    m = Middle_cart.objects.all().filter(product_id=product_id)
    try:
        m = m[0]
        p = int(m.purchase_number) + int(numbers)
        m.delete()
    except:
        p = numbers
    Middle_cart.objects.create(cart_id=cartid, product_id=product_id, purchase_number=p)


class BuyingView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Middle_cart.objects.all()
    serializer_class = BuyingSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        this method get query params and create middle cart

        """
        query_params = self.request.query_params.items()
        for product_id, numbers in query_params:
            createmiddlecart(self, request, product_id, numbers)
            serializer = BuyingSerializer(self.queryset, many=True)
        return Response(serializer.data)


class FactorView(viewsets.ModelViewSet):
    """
    this class view inheritance from ModelViewSet and have all CRUD API methods

    """
    queryset = Finance.objects.all()
    serializer_class = FactorSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
        this method record user buying and update product number

        """
        cart = Cart.objects.get(user_id=request.user.id)
        middlecart = Middle_cart.objects.all().filter(cart_id=cart.id)
        for elm in middlecart:
            elm.product.number = int(elm.product.number) - 1
            elm.product.save()
        Finance.objects.create(user=request.user.username, cart=cart.id, total_price=cart.totalprices,
                               number_product=cart.TotalPro, done=True)
        serializer = FactorSerializer(self.queryset, many=True)
        return Response(serializer.data)



