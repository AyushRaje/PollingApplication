from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

# class Users(models.Model):
#     username=models.CharField(max_length=100)

#     def __str__(self):
#         return self.username

class Question(models.Model):
    session_id=models.CharField(max_length=10,blank=False,null=True,default="ADMIN01")
    content=models.CharField(max_length=256)
    users_answered=models.ManyToManyField(User,blank=True)
    def __str__(self):
        return self.content

class Choice(models.Model):
    content=models.CharField(max_length=100)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    vote=models.IntegerField(default=0)
    def __str__(self):
        return "{}-{}".format(self.question.content[:30],self.content)

