from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from poller import models
from django.urls import reverse
from django.contrib import messages
from session import models as session_models

# Create your views here.
@login_required(login_url='/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    
    
    
    Context={
        "question_content":models.Question.objects.all,
        "choice_content":models.Choice.objects.all,
    }
    return render(request,'questions.html',Context)








