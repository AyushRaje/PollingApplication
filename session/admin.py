from django.contrib import admin
from session import models
from django.contrib.sessions.models import Session
# Register your models here.
admin.site.register([
    Session,
    models.UserSession,
    models.SessionsCreated
])