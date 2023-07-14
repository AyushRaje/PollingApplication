from django.contrib import admin
from poller import models
# Register your models here.
admin.site.register([
    models.Question,
    models.Choice
])