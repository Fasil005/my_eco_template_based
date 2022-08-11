from django.shortcuts import render,redirect
from accounts.models import User

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Statements
from .serializers import StatementsSerializer

global first_data 
first_data = [{'date':0,'amount': 0, 'type' : 0, 'purpose' : 0, 'balance' : 0}]

def find_details(userID, is_statements=False):
    user = User.objects.get(id=userID)
    statements = Statements.objects.filter(u_id=userID).order_by('-id').all()
    main_balance = list(statements)[0].balance if list(statements) != [] else 0
    if is_statements:
        return (user.fullname, main_balance, statements)
    return (user.fullname, main_balance,)

def index(request):
    if 'id' in request.session.keys():
        userID = request.session['id']
        fullname, main_balance, statements = find_details(userID=userID, is_statements=True)
        return render(request, 'index.html', {'statements': statements,'main_balance':main_balance, 'user': fullname})
    else:
        return redirect('/')

def expense(request):

    if 'id' in request.session.keys():
        userID = request.session.get('id')
        fullname, main_balance = find_details(userID=userID)
        return render(request, 'expense.html', {'user': fullname, 'main_balance':main_balance,})
    else:
        return redirect('/')

def income(request):
    
    if 'id' in request.session.keys():
        userID = request.session.get('id')
        fullname, main_balance = find_details(userID=userID)
        return render(request, 'income.html', {'user': fullname, 'main_balance':main_balance,})
    else:
        return redirect('/')

def loan(request):
   
    if 'id' in request.session.keys():
        userID = request.session.get('id')
        fullname, main_balance = find_details(userID=userID)
        return render(request, 'loan.html', {'user': fullname, 'main_balance':main_balance,})
    else:
        return redirect('/')


class ADDBalance(APIView):
    
    def post(self, request, *args, **kwargs):
        
        data = request.data.copy()
        data['u_id'] = request.session['id']
        data['amount'] = 0
        data['type'] = 'BASE_BALANCE'
        data['purpose'] = 'BASE_BALANCE'
        serializer = StatementsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
        return redirect('/my_eco/')
        


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