from django.urls import path
from . import views 
urlpatterns=[
  path('',views.index,name='index'),
  path('home/',views.home,name='home'),
  path('list/',views.list,name='list'),
  path('listform/',views.form1,name='listform'),
  path('signup/',views.signup,name='signup'),
  
 ]