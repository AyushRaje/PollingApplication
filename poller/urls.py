from django.urls import path
from poller import views
urlpatterns = [
    path('',views.index,name='index'),
    path('vote/',views.vote,name='vote'),
    path('results/',views.results,name="results")
]
