from django.shortcuts import render,redirect
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer

# Create your views here.
def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            print(data)
            return redirect('/')
        error=""
        for i in serializer.errors:
            error = serializer.errors.get(i)[0].replace('This',i)
            break
        return render(request, 'register.html', {'msg': error})



class Login(APIView):
    def post(self, request):
        
        user = User.objects.filter(username = request.data['username']).first()
        
        if user is not None:
         
            if user.password == request.data['password']:
                print(user.id)
                request.session['id'] = user.id
                return redirect('/my_eco')
            else:
                return render(request, 'login.html', {'msg': 'Wrong Password'})
        else:
            return render(request, 'login.html', {'msg': 'Wrong Username'})