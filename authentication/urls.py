from django.urls import path
from authentication import views
from django.views.generic.base import TemplateView
urlpatterns=[
    path('',views.Log_in,name='login'),
    path('login/',views.Log_in,name='login'),
    path('logout/',views.Log_out,name='logout'),

]