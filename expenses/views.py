from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer

class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class ExpenseSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        period = request.query_params.get('period', 'monthly')

        qs = Expense.objects.filter(user=request.user)

        total = qs.aggregate(total_spent=Sum('amount'))['total_spent'] or 0

        return Response({
            "period": period,
            "total_spent": total
        })

class CategoryBreakdownView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = (
            Expense.objects
            .filter(user=request.user)
            .values('category__name')
            .annotate(total=Sum('amount'))
            .order_by('-total')
        )

        return Response(data)

class TopCategoriesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = (
            Expense.objects
            .filter(user=request.user)
            .values('category__name')
            .annotate(total=Sum('amount'))
            .order_by('-total')[:5]
        )

        return Response(data)


