from rest_framework import serializers
from .models import Category, Expense

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        source="category",
        queryset=Category.objects.all(),
        write_only=True
    )
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Expense
        fields = [
            "id",
            "amount",
            "category",
            "category_id",
            "date",
            "created_at",
            "updated_at",
        ]
     
