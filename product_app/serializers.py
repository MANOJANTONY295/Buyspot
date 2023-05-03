from rest_framework import serializers
from product_app.models import Category, Product,Cart,MyOrder,Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class   ProductSerializer(serializers.ModelSerializer):
    # rating = serializers.StringRelatedField()
    class Meta:
        model =Product
        fields = ['id', 'item','Image', 'price','offer','size', 'category', 'stock', 'rating','description']

# class RatingSerializer(serializers.ModelSerializer):
#     #  rating = serializers.StringRelatedField() 
#      class Meta:
#         model = Item_Rating
#         fields = ['item', 'one', 'two','three', 'four', 'five']     

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields =['id','item','image','size','quantity', 'price', 'total']

class MyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =MyOrder    
        fields =['user','product_name','quantity','ordered']    

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('product_name', 'total_product')
 


#test

from rest_framework import serializers
from .models import YourModel

class YourSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = ('id', 'name', 'description')




        