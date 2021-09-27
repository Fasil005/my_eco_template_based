from django.shortcuts import render, get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Statements
from .serializers import StatementsSerializer
from django.http import HttpResponse


def index(request):
    statements = Statements.objects.all()
    return render(request, 'index.html', {'statements': statements})

def expense(request):
    return render(request, 'expense.html', {})

class ADDExpense(APIView):
    # permission_classes = [AllowAny]
    def post(self, request):
        balance = Statements.objects.order_by('-id').first().balance
        data = request.data.copy()
        data['balance'] = float(balance) - float(data['amount'])
        serializer = StatementsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return render(request, 'expense.html', {})