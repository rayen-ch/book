from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from myshop.products.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)  # optional
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

    class Meta:
        unique_together = ('product', 'user')

    def total_upvotes(self):
        return self.votes.filter(value=1).count()

    def total_downvotes(self):
        return self.votes.filter(value=-1).count()

class Vote(models.Model):
    UP = 1
    DOWN = -1
    VALUE_CHOICES = [
        (UP, 'Positive'),
        (DOWN, 'Negative'),
    ]

    review = models.ForeignKey(Review, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.IntegerField(choices=VALUE_CHOICES)  # NOT NULL Feld

    class Meta:
        unique_together = ('review', 'user')
