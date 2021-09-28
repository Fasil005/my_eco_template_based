from django.shortcuts import render,redirect

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Statements
from .serializers import StatementsSerializer


def index(request):
    statements = Statements.objects.order_by('-id').all()
    main_balance = list(statements)[0].balance
    return render(request, 'index.html', {'statements': statements,'main_balance':main_balance})

def expense(request):
    return render(request, 'expense.html', {})


def income(request):
    return render(request, 'income.html', {})

def loan(request):
    return render(request, 'loan.html', {})


class ADDExpense(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        balance = Statements.objects.order_by('-id').first().balance
        data = request.data.copy()
        data['balance'] = float(balance) - float(data['amount'])
        data['type'] = 'EXPENSE'
        if data['balance'] < 0:
            return render(request, 'expense.html', {'msg':'Insufficient Funds'})
        serializer = StatementsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return redirect('/')
        error=""
        for i in serializer.errors:
            error = serializer.errors.get(i)[0].replace('This',i)
            break
        return render(request, 'expense.html', {'msg': error})




class ADDIncome(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        balance = Statements.objects.order_by('-id').first().balance
        data = request.data.copy()
        data['balance'] = float(balance) + float(data['amount'])
        data['type'] = 'INCOME'
        serializer = StatementsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return redirect('/')
        error=""
        for i in serializer.errors:
            error = serializer.errors.get(i)[0].replace('This',i)
            break
        return render(request, 'expense.html', {'msg': error})


class ADDLoan(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        balance = Statements.objects.order_by('-id').first().balance
        data = request.data.copy()
        if data['from/to'] == 'From':
            data['balance'] = float(balance) + float(data['amount'])
        else:
            data['balance'] = float(balance) - float(data['amount'])
            if data['balance'] < 0:
                return render(request, 'loan.html', {'msg':'Insufficient Funds'})
        data['purpose'] = data['from/to'] +" "+ data['purpose']
        data['type'] = 'LOAN'
        serializer = StatementsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return redirect('/')
        error=""
        for i in serializer.errors:
            error = serializer.errors.get(i)[0].replace('This',i)
            break
        return render(request, 'expense.html', {'msg': error})