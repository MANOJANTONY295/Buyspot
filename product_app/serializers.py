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
        #Fields = '__all__'

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
<<<<<<< HEAD
        fields =['user','product','quantity','ordered']    
=======
        fields =['user','order_id','ordered_item','quantity','price','ordered_on','delivered_on']
>>>>>>> 0a404a4e2440a38996b758c7737eb8889fa60560

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('product', 'total_product','transaction_id','total_amount','created_at','updated_at')

#check manoj

from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'customer_name', 'order_id', 'amount', 'payment_date', 'payment_status', 'payment_mode', 'Payment_id')

 
 #check manoj

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'





        
