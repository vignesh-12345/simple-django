from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=password.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    else:
        


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                #print('user already exists') it will print this on console or terminal
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                #print('email already exists')
                messages.info(request,'Email already exits')
                return redirect('register')
            else:    
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                User.save();
                print('user created')
         
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
