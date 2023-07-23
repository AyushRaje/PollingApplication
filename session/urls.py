from django.urls import path
from session import views
urlpatterns = [
    path('',views.CreateSession,name='createsession')
]
