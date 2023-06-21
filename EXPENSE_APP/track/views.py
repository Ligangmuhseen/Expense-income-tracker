from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,'index.html')


def index1(request):
    return render(request,'index1.html')    


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(username=username,password=Password)

        if user is not None:
            auth.login(request,user)
            return redirect('/index')

        else:
            return redirect("/login")    




    else:
        return render(request,'login.html')




def registration(request):

    if request.method == 'POST':
        username = request.POST['username']
        Email = request.POST['email']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']

        user = User.objects.create_user(username=username,password=Password1,email=Email)
        user.save()
        print('user created')
        return redirect('/')

    else:    
        return render(request,'registration.html')    


