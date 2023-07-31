from django.urls import path
from session import views
urlpatterns = [
    path('createsession/',views.CreateSession,name='createsession'),
    path('createsession/',views.ShowCreatedQuestions,name='showcreatedquestions'),
    path('',views.ShowQuestions,name='showquestions'),
    path('results/',views.Results,name='results'),
    path('vote/',views.vote,name='vote'),
    path('delete/<int:ques_id>',views.Delete,name='delete'),
    path('edit/<int:ques_id>',views.Edit,name='edit'),
    path('createdsessions/',views.ShowCreatedSessions,name='sessionscreated'),
    path('deletesession/<sessions>',views.DeleteSession,name='deletesession'),
    path('editsession/<sessions>', views.EditSession,name='editsession'),
    path('deleteeditsession/<int:ques_id>',views.DeleteEditSession,name='deleteeditsession'),
    path('editeeditsession/<int:ques_id>',views.EditEditSession,name='editeditsession'),
    path('editsession/',views.ShowEditedQuestions,name='showeditedquestions'),
]
