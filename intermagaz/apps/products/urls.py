from django.urls import path
from apps.products.views import ProductAPIView


urlpatterns = [
    path('', ProductAPIView.as_view(), name='product-list')



]