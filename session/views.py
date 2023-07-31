from django.shortcuts import render,redirect,get_object_or_404
from poller import models
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from session import models as session_models
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def ShowCreatedQuestions(request):
    sid='{}'.format(request.session.session_key[:6])
    questions=models.Question.objects.all()
    context={
        'id':sid,
        'question':questions,
        'session_key':request.session.session_key
    }
    return render(request, 'session.html',context)

@login_required(login_url='/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def CreateSession(request):
    sid='{}'.format(request.session.session_key[:6])
    questions=models.Question.objects.all()
    context={
        'id':sid,
        'question':questions,
        'session_key':request.session.session_key
    }
    session_added=False
    for session in session_models.SessionsCreated.objects.all():
        if session.session_id==sid:
            session_added=True

    if not session_added:
        add_session=session_models.SessionsCreated.objects.create(session_id=sid)
        add_session.save()        
    user_created_session=session_models.UserSession.objects.get(user=request.user)
    session_id_add=session_models.SessionsCreated.objects.get(session_id=sid)
    user_created_session.sessions_created.add(session_id_add)
    user_created_session.save()

    if request.method=='POST':
        new_question=models.Question.objects.create()
        new_question.session_id=sid
        new_question.content=request.POST['entered_question']
        new_question.save()
        for i in range(1,5):
            choice="choice"+str(i)
            try:
                if request.POST[choice]!='':
                    new_choice=models.Choice.objects.create(question=new_question)
                    new_choice.content=request.POST[choice]
                    new_choice.save()
            except:
                continue        
        return redirect('showcreatedquestions')      
        
    return render(request,'session.html',context)

@login_required(login_url='/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

@login_required(login_url='/login/')   
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Results(request):
    entered_id=request.session['id']
    questions=models.Question.objects.all()
    context={
        'questions':questions,
        'id':entered_id
    }
    return render(request,'results.html',context)

@login_required(login_url='/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
                return redirect('showquestions')

        if not has_answered:
            selected_choice.vote+=1
            selected_choice.save()
            selected_ques.users_answered.add(request.user.id)
            selected_ques.save()          
    except:
        messages.warning(request,"Please select an Option")
        return redirect('showquestions') 
    
    return redirect('showquestions')

def Delete(request,ques_id):
    question=models.Question.objects.filter(pk=ques_id)
    question.delete()
    return redirect('createsession')    

def Edit(request,ques_id):
    CreateSession(request)
    question=models.Question.objects.filter(pk=ques_id)
    question.delete()
    return redirect(reverse('createsession'))

def ShowCreatedSessions(request):
    try:
        session_user=session_models.UserSession.objects.get(user_id=request.user.id)
        sessions_created=session_user.sessions_created.all()
        context={
            "sessions_created":sessions_created
        }

        return render(request, 'sessions_created.html',context)
    except ObjectDoesNotExist:
        messages.error(request,"No Existing Sessions Present")
        return redirect('index')
    
@login_required(login_url='login/')
def DeleteSession(request,sessions):
    session_to_delete=session_models.SessionsCreated.objects.get(session_id=sessions)
    session_to_delete.delete()
    for questions in models.Question.objects.all():
        if questions.session_id==sessions:
            questions.delete()
    return redirect('sessionscreated')

def EditSession(request,sessions):
    sid=sessions
    request.session['sid']=sid
    questions=models.Question.objects.all()
    context={
        'id':sid,
        'question':questions,
        'session_key':sessions
    }
    if request.method=='POST':
        new_question=models.Question.objects.create()
        new_question.session_id=sid
        new_question.content=request.POST['entered_question']
        new_question.save()
        for i in range(1,5):
            choice="choice"+str(i)
            try:
                if request.POST[choice]!="":
                    new_choice=models.Choice.objects.create(question=new_question)
                    new_choice.content=request.POST[choice]
                    new_choice.save()
            except:
                continue        
        return redirect('showeditedquestions')   
        
    return render(request,'edit_session.html',context)

def DeleteEditSession(request,ques_id):
    sid=request.session.get('sid')
    question=models.Question.objects.filter(pk=ques_id)
    question.delete()
    return redirect(reverse('editsession',kwargs={"sessions":sid}))

def EditEditSession(request,ques_id):
    sid=request.session.get('sid')
    EditSession(request,sid)
    question=models.Question.objects.filter(pk=ques_id)
    question.delete()
    return redirect(reverse('editsession',kwargs={"sessions":sid}))

def ShowEditedQuestions(request):
    sid=request.session.get('sid')
    print(sid)
    questions=models.Question.objects.all()
    context={
        'id':sid,
        'question':questions,
        'session_key':request.session.session_key
    }
    return render(request, 'edit_session.html',context)
