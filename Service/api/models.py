from django.contrib.auth.models import User
from django.db import models
from django.db.models import Manager


def get_user():
    user=User.objects.all()
    return user
class Category(models.Model):
    name=models.CharField(max_length=50)

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super(AvailableManager, self).get_queryset().filter(is_available=True)

class Product(models.Model):
    name=models.CharField(max_length=150)
    slug=models.SlugField(unique=True, null=False, blank=False)
    price=models.CharField(max_length=50)
    category=models.ManyToManyField(Category, related_name='category')
    image=models.ImageField(upload_to='')
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    is_availabele=AvailableManager()

    def __str__(self):
        return self.name
class Profile(models.Model):
    user=models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='')
    total_price=models.PositiveIntegerField(default=True)

    def __str__(self):
        return self.user.username

class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='username')
    count=models.IntegerField(default=True)
    product_name=models.ForeignKey(Product, related_name='product')

    def total_sum(self, price):
        total_price=self.product.price+self.cart.count



