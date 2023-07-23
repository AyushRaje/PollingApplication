from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from poller import models
from django.urls import reverse
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    Context={
        "question_content":models.Question.objects.all,
        "choice_content":models.Choice.objects.all
    }
    return render(request,'questions.html',Context)

def vote(request):
    has_answered=False    
    try:   
        selected_choice=models.Choice.objects.get(pk=request.POST['choice'])
        selected_ques=models.Question.objects.get(pk=selected_choice.question_id)
        All_users=selected_ques.users_answered.all()
        for users in All_users:    
            if users.id==request.user.id:
                has_answered=True
                messages.warning(request,"Already answered")
                break
        if not has_answered:
            selected_choice.vote+=1
            selected_choice.save()
            selected_ques.users_answered.add(request.user.id)
            selected_ques.save()          
    except:
        messages.warning(request,"Please select an Option")
        redirect('index')   

    return redirect(reverse('index'))

@login_required(login_url='/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def results(request):
    if request.user.id:
        context={
            "question_content":models.Question.objects.all
        }
        return render(request,'results.html',context)




