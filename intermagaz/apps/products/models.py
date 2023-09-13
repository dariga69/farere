from django.db import models
from apps.categories.models import Category
from apps.users.models import User


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    country = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product')

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_like')

    def __str__(self):
        return f"{self.user} - {self.product}"


def post(self, request, *args, **kwargs):
    user = request.user
    product_id = request.data['product']
    product = Product.objects.get(id=product_id)
    like_obj = Like.objects.filter(product=product, user=user).first()
    if like_obj:
        like_obj.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
    else:
        like = Like.objects.create(user=user, product=product)
        return Response({"message": "Created"}, status=status.HTTP_201_CREATED)


