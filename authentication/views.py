from django.shortcuts import render,redirect
from authentication import forms
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.views.generic import(
    DetailView,
    ListView,
)
from authentication import models
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect



def Log_in(request):
    if request.method=='GET':
        login_form=forms.LoginForm()
        context={
            "form":login_form
        }
        return render(request,'login.html',context)
    
    if request.method=='POST':
        login_form=forms.LoginForm(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data["username"]
            password=login_form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                context={
                    "current_user":username
                }
                return redirect('index')
            else:
                messages.error(request,f'Invalid username or password')
                return redirect('login')
            

def Log_out(request):
    logout(request)
    return redirect('login')


    







        