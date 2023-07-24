from django.urls import path
from poller import views
urlpatterns = [
    path('',views.index,name='index')
    
]
