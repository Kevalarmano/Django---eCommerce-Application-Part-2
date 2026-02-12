from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ("buyer", "Buyer"),
        ("vendor", "Vendor"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="buyer")

    def is_vendor(self) -> bool:
        return self.role == "vendor"

    def is_buyer(self) -> bool:
        return self.role == "buyer"


class Store(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stores")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="store_logos/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} (vendor={self.vendor.username})"


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} @ {self.store.name}"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(default=5)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review({self.product.name}, {self.rating})"
