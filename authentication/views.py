from django.shortcuts import render,redirect
from authentication import forms
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.db.utils import IntegrityError 
from session import models as session_models

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
                sid='{}'.format(request.session.session_key[:6])
                add_session=session_models.SessionsCreated.objects.create(session_id=sid)
                add_session.save()
                return redirect('index')
            else:
                messages.error(request,f'Invalid username or password')
                return redirect('login')
            

def Log_out(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method=='GET':
        signup_form=forms.SignupForm()
        context={
            'form':signup_form
        }
        return render(request,'signup.html',context)

    if request.method=='POST':
        signup_form=forms.SignupForm(request.POST)
        context={
            'form':signup_form,
            'username_error':False,
            'pass_error':False
        }
        username=signup_form['username']
        for users in User.objects.all():
                if users.username==username:
                    print(users.username)
                    context['username_error']=True
                    break 

        if signup_form.is_valid():
                   
            if context['username_error']==False:
                username=signup_form.cleaned_data['username']
                password=signup_form.cleaned_data['password']
                cnf_password=signup_form.cleaned_data['cnf_password'] 

                if password!=cnf_password:
                    context['pass_error']=True
                    return render(request,'signup.html',context)
                
                else:
                    try:
                        new_user=User.objects.create_user(username=username,password=password)
                        new_user.save()
                        messages.success(request,message="Signed in Successfully")
                        AddUserSession(request,new_user)
                        context['username_error']=False
                        context['pass_error']=False
                    except IntegrityError as err:
                        context['username_error']=True
                        return render(request,'signup.html',context)  
                    
                    return redirect('login')   
                    
    return render(request,'signup.html',context)
    
def AddUserSession(request,user):
    addsession=session_models.UserSession.objects.create(user=user)
    addsession.save()






        