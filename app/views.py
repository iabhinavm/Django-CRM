from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import  messages
from .forms import SignUpForm,AddRecordForm
from .models import Customer
# Create your views here.
def home(request):
    record=Customer.objects.all
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
        return render(request,'home.html',{'records':record})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,"Sucessfully Loged oUt")
    return redirect('home')
    
def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #auntenticate
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully logedIn")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record=Customer.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You must login first")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it=Customer.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"You have successfuly deleted the record")
        return redirect('home')
    else:
        messages.success(request,"You must login first")
        return redirect('home')
    
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Customer.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form,'customer_record':current_record})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
