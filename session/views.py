from django.shortcuts import render,redirect
from poller import models
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def CreateSession(request):
    sid='{}'.format(request.session.session_key[:6])
    questions=models.Question.objects.all()
    context={
        'id':sid,
        'question':questions,
        'session_key':request.session.session_key
    }
    if request.method=='POST':
        new_question=models.Question.objects.create()
        new_question.session_id=sid
        new_question.content=request.POST['entered_question']
        new_question.save()
        for i in range(1,5):
            choice="choice"+str(i)
            if request.POST[choice]!='':
                new_choice=models.Choice.objects.create(question=new_question)
                new_choice.content=request.POST[choice]
                new_choice.save()

    return render(request,'session.html',context)

def ShowQuestions(request):
    questions=models.Question.objects.all()
    if request.method=='POST':
        entered_id=request.POST['session_id']
        request.session['id']=entered_id
    context={
            'session_questions':questions,
            'entered_id':request.session['id']
    }    
    
    return render(request,'session_questions.html',context)
    
def Results(request):
    entered_id=request.session['id']
    questions=models.Question.objects.all()
    context={
        'questions':questions,
        'id':entered_id
    }
    return render(request,'results.html',context)

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
        return redirect('showquestions') 

    return redirect('showquestions')