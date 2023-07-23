from django.shortcuts import render,redirect
from poller import models
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def CreateSession(request):
    sid='{}'.format(request.session.session_key[:6])
    questions=models.Question.objects.all()
    context={
        'id':sid,
        'question':questions
    }
    if request.method=='POST':
        new_question=models.Question.objects.create()
        new_question.session_id=sid
        new_question.content=request.POST['question']
        new_question.save()
        for i in range(1,5):
            choice="choice"+str(i)
            if request.POST[choice]!='':
                new_choice=models.Choice.objects.create(question=new_question)
                new_choice.content=request.POST[choice]
                new_choice.save()

    return render(request,'session.html',context)