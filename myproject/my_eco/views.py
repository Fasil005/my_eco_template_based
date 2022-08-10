from django.shortcuts import render,redirect
from accounts.models import User

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Statements
from .serializers import StatementsSerializer

global first_data 
first_data = [{'date':0,'amount': 0, 'type' : 0, 'purpose' : 0, 'balance' : 0}]

def index(request):
    if 'id' in request.session.keys():
        userID = request.session['id']
        user = User.objects.filter(id=userID).values('fullname')
        statements = Statements.objects.filter(u_id=userID).order_by('-id').all()
        main_balance = list(statements)[0].balance if list(statements) != [] else 0
        statements = first_data if list(statements) == [] else statements
        
        return render(request, 'index.html', {'statements': statements,'main_balance':main_balance, 'user': user[0]['fullname']})
    else:
        return redirect('/')

def expense(request):

    if 'id' in request.session.keys():
        userID = request.session.get('id')
        user = User.objects.get(id=userID)
        statements = Statements.objects.filter(u_id=userID).order_by('-id').all()
        main_balance = list(statements)[0].balance if list(statements) != [] else 0
        return render(request, 'expense.html', {'user': user.fullname, 'main_balance':main_balance,})
    else:
        return redirect('/')

def income(request):
    
    if 'id' in request.session.keys():
        userID = request.session.get('id')
        user = User.objects.get(id=userID)
        statements = Statements.objects.filter(u_id=userID).order_by('-id').all()
        main_balance = list(statements)[0].balance if list(statements) != [] else 0
        return render(request, 'income.html', {'user': user.fullname, 'main_balance':main_balance,})
    else:
        return redirect('/')

def loan(request):
   
    if 'id' in request.session.keys():
        userID = request.session.get('id')
        user = User.objects.get(id=userID)
        statements = Statements.objects.filter(u_id=userID).order_by('-id').all()
        main_balance = list(statements)[0].balance if list(statements) != [] else 0
        return render(request, 'loan.html', {'user': user.fullname, 'main_balance':main_balance,})
    else:
        return redirect('/')


class ADDExpense(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        userID = request.session['id']
        balance = Statements.objects.filter(u_id=userID).order_by('-id').first().balance
        data = request.data.copy()
        data['u_id'] = userID
        data['balance'] = float(balance) - float(data['amount'])
        data['type'] = 'EXPENSE'
        if data['balance'] < 0:
            return render(request, 'expense.html', {'msg':'Insufficient Funds'})
        serializer = StatementsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return redirect('/my_eco/')
        error=""
        for i in serializer.errors:
            error = serializer.errors.get(i)[0].replace('This',i)
            break
        return render(request, 'expense.html', {'msg': error})




class ADDIncome(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        userID = request.session['id']
        balance = Statements.objects.filter(u_id=userID).order_by('-id').first().balance
        data = request.data.copy()
        data['u_id'] = userID
        data['balance'] = float(balance) + float(data['amount'])
        data['type'] = 'INCOME'
        serializer = StatementsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return redirect('/my_eco/')
        error=""
        for i in serializer.errors:
            error = serializer.errors.get(i)[0].replace('This',i)
            break
        return render(request, 'expense.html', {'msg': error})


class ADDLoan(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        userID = request.session['id']
        balance = Statements.objects.filter(u_id=userID).order_by('-id').first().balance
        data = request.data.copy()
        data['u_id'] = userID
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
            print('hi')
            return redirect('/my_eco/')
        error=""
        for i in serializer.errors:
            error = serializer.errors.get(i)[0].replace('This',i)
            break
        return render(request, 'expense.html', {'msg': error})