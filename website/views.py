from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    #check to see logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You Have been LoggedIn!')
            return redirect('home')
        else:
            messages.success(request,'Something went wrong! try again')
            return redirect('home')
    else:
        return render(request, 'home.html',{})
def logoutUser(request):
    logout(request)
    messages.success(request, 'You Are Logged Out!')
    return redirect('home')