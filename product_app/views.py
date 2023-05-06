
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from product_app.models import *
from product_app.serializers import *
from .models import Payment
from .serializers import PaymentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

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





class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

