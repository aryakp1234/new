from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'index.html')
def loginn(request):
    return render (request,'login.html')
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        myuser = User.objects.create_user(username,password)
    return render(request,'signup.html')
