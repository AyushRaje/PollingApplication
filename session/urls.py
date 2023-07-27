from django.urls import path
from session import views
urlpatterns = [
    path('createsession/',views.CreateSession,name='createsession'),
    path('',views.ShowQuestions,name='showquestions'),
    path('results/',views.Results,name='results'),
    path('vote/',views.vote,name='vote'),
    path('delete/<int:ques_id>',views.Delete,name='delete'),
    path('edit/<int:ques_id>',views.Edit,name='edit')
]
