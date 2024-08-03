from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import  messages
# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You Have Succesfully Loged in")
            return redirect('home')
        else:
            messages.success(request,"Enter valid Email/PASSWORD")
            return redirect('home')
    else:
        return render(request,'home.html',{})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,"Sucessfully Loged oUt")
    return redirect('home')
    
def register_user(request):
    return render(request,'register.html',{})