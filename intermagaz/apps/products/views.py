from rest_framework import generics
from apps.products.models import Product
from apps.products.serializers import ProductSerializer



class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LikeAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        user = request.user
        products = Product.objects.filter(product_like__user=user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data['product']
        product = Product.objects.get(id=product_id)
        like = Like.objects.create(user=user, product=product)
        return Response({"message": "Created"}, status=status.HTTP_201_CREATED)