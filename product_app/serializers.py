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
        fields = ['id', 'name','Image', 'price','offer','size', 'category', 'stock', 'rating','description']
        #Fields = '__all__'

# class RatingSerializer(serializers.ModelSerializer):
#     #  rating = serializers.StringRelatedField() 
#      class Meta:
#         model = Item_Rating
#         fields = ['item', 'one', 'two','three', 'four', 'five']     

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields =['id','name','image','size','quantity', 'price', 'total']

class MyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =MyOrder    
        fields =['user','product_name','quantity','ordered']    

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('product_name', 'total_product')

#check manoj

from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'customer_name', 'order_id', 'amount', 'payment_date', 'payment_status', 'payment_mode', 'Payment_id')

 





        