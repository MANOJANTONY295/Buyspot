from django import views
from django.conf import settings
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static

from product_app.views import CategoryViewSet, ProductViewSet,CartViewSet,MyOrderViewSet,OrderViewSet, SearchView


router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'myorder',MyOrderViewSet)
router.register(r'order',OrderViewSet)

# router.register(r'rating',RatingViewSet)


urlpatterns = [
   path('', include(router.urls)),
   # path('api/', include('rest_framework.urls', namespace='rest_framework'))
   path('search/', SearchView.as_view())

   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)