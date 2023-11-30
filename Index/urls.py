from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),

    path('auditorium',views.auditorium,name='auditorium'),
    path('selfie' , views.selfie , name='selfie'),
    path('selfie2' , views.selfie2 , name='selfie2'),
    path('selfie3' , views.selfie3 , name='selfie3'),
    path('project' , views.project , name='project'),
    path('archive' , views.archive , name='archive'),
]
