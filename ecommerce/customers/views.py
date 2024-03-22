from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Customer
from django.contrib import messages

def sign_out(request):
    logout(request)
    return redirect('home')

def show_account(request):
    context={}
    if request.method == 'POST' and 'register' in request.POST:
    
        context['register']=True

        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            
            # Check if a user with the same username already exists
            if User.objects.filter(username=username).exists():
                # If a user with the same username exists, display an error message
                messages.error(request, 'User already exists!!!')
                return redirect('register')  # Redirect to the registration page or account creation page
                
            # Create the user account
            user = User.objects.create_user(
                name=username,
                username=username,
                password=password,
                email=email
            )
            
            # Create the customer account
            customer = Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            
            # Redirect to home page after successful account creation
            # return redirect('home')
            success_message="user registered successfully!!"
            messages.success(request,success_message )

        
        except Exception as e:
            # Handle any other exceptions that may occur during user or customer creation
            error_message = "invalid credatial"
            messages.error(request, error_message )
            return redirect('register')  # Redirect to the registration page or account creation page with error message
    
    if request.method == 'POST' and 'login' in request.POST:
         context['register']=False
         username = request.POST.get('username')
         password = request.POST.get('password')
         user= authenticate(username=username,password=password)
         if user:
            login(request,user) 
            return redirect('home')
         else:
            messages.error(request,'invalid user credentials' )
             
            


    return render(request, 'account.html',context)
