from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import UserAddForm
from .blockgenerator import Block
from datetime import datetime
from .models import Block_1
from .decorators import admin_only
from landdeals.models import Properties


@admin_only
def Index(request):
    proper = Properties.objects.all()
    context = {
        "proper":proper
    }
    return render(request,"index.html",context)

def LandLoardIndex(request):
    return render(request,"landloardindex.html")

def UserTypeConfirmation(request):
    return render(request,"usertypeconfirmation.html")

def LandLoadConfirm(request):
    user = request.user 
    group = Group.objects.get(name="landloard")
    user.groups.add(group)
    user.save()
    return redirect('Index')

def TenentConfirm(request):
    user = request.user 
    group = Group.objects.get(name="tenent")
    user.groups.add(group)
    user.save()
    return redirect('Index')

def SignIn(request):
    if request.method == "POST":
        uname = request.POST['uname']
        password = request.POST["pswd"]
        user = authenticate(request,username= uname, password = password)
        if user is not None:
            login(request,user)
            return redirect('Index')
        else:
            messages.info(request,"Username or Password Incorrecr")
            return redirect('SignIn')
    return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            email = user.email 
            password = user.password
            username = user.username
            regdata = {"name":username,'email':email,"password":password}
            
            BlockChain = Block(1, datetime.now(), regdata,"0")
            
            block = Block_1.objects.create(BlockIndex = 1,BlockTimeStrap = datetime.now(),BlockLink = user,BlockData = regdata,previous_hash = "0",Blockhash = BlockChain.hash)
            block.save()
            
            messages.info(request,"User Created")
            return redirect('SignIn')
    return render(request,"register.html",{"form":form})

def SignOut(request):
    logout(request)
    return redirect('SignIn')

def SearchProperty(request):
    if request.method =="POST":
        value = request.POST['search']
        proper = Properties.objects.filter(place__contains = value)
        if len(proper) == 0:
            flag = 0
        else:
            flag = 1
        return render(request,'searchedproperties.html',{"proper":proper,"flag":flag})
        
        
        
        
    return redirect("Index")