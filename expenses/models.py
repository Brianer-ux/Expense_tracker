from django.db import models
from django.contrib.auth.models import User
 
class Category(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="categories"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


    class Meta:
        unique_together = ("user", "name")


    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expenses"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='expenses'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.amount} on {self.date}"
