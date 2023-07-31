from django.db import models
from django.contrib.auth.models import User
from poller import models as poller_models
from django.contrib.sessions.models import Session

class SessionsCreated(models.Model):
    session_id=models.CharField(max_length=6,unique=True)
    
    def __str__(self):
        return self.session_id

# Create your models here.
class UserSession(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    sessions_created=models.ManyToManyField(SessionsCreated,blank=True)
    
    def __str__(self):
        return self.user.username