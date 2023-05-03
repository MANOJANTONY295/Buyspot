
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

#test

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import YourModel
from .serializers import YourSerializer

class SearchView(APIView):
    def get(self, request, format=None):
        query = request.GET.get('q', '')
        results = YourModel.objects.filter(name__icontains=query)
        serializer = YourSerializer(results, many=True)
        return Response(serializer.data)



