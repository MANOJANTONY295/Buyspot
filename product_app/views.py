
from django.shortcuts import get_object_or_404, render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import generics
from rest_framework import viewsets
from product_app.models import *
from product_app.serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class RatingViewSet(viewsets.ModelViewSet):
#     queryset = Item_Rating.objects.all().order_by('?') 
#     serializer_class = RatingSerializer   

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class MyOrderViewSet(viewsets.ModelViewSet):
    queryset = MyOrder.objects.all()
    serializer_class = MyOrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    

#test manoj
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from .models import Product
# from .serializers import ProductSerializer
# from rest_framework.filters import SearchFilter


# class SearchAPIView(APIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['item', 'price']

    # def get(self, request, format=None):
    #     query = request.GET.get(all)

    #     if not query:
    #         return Response([])

    #     queryset = Product.objects.filter(name__icontains=query)
    #     serializer = ProductSerializer(queryset, many=True)

    #     return Response(serializer.data)

    #test manoj

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductSearchAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()

        # Apply filters if present in the request query params
        name = request.query_params.get('name', None)
        category = request.query_params.get('category', None)
        min_price = request.query_params.get('min_price', None)
        max_price = request.query_params.get('max_price', None)

        if name:
            products = products.filter(name__icontains=name)
        if category:
            products = products.filter(category=category)
        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

#check manoj

from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer



class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductPopularity
from .serializers import ProductSerializer


class PopularProductsAPIView(APIView):
    def get(self, request, format=None):
        # Get the top 10 most popular products
        popular_products = ProductPopularity.objects.order_by('-popularity')[:10]
        product_ids = [pp.product.id for pp in popular_products]
        products = Product.objects.filter(id__in=product_ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # Increment the popularity count for the given product
        product_id = request.data.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            popularity, created = ProductPopularity.objects.get_or_create(product=product)
            popularity.popularity += 1
            popularity.save()
            return Response(status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


