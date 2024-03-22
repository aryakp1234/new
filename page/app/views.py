from django.shortcuts import render,redirect
from . models import *
from . forms import *
from django.contrib.auth import authenticate,login
# from django.shortcuts import render,redirect

# Create your views here.

   
def index(request):
    if request.method =='POST':
         username = request.POST['username']
         password = request.POST['password']
         user= authenticate(request,username=username,password=password)
         if user is not None:
              login(request,user)
              return redirect('home')
    return render(request,'login.html')    

def signup(request) :
    return render(request,'signup.html')


    
def home(request):
    return render(request,'home.html')

  

def list(request):
    s=Signin.objects.all()
    content={'data':s}
    return render(request,'list.html',content)

def form1(request):
    f1=listform()
    if (request.method=='POST'):
        f1=listform(request.POST)
        if f1.is_valid():
            f1.save()
            return list(request)
    return render(request,'listform.html',{'form':f1})    