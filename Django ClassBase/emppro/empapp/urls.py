from django.contrib import admin
from django.urls import path
from .views import Emplist,Empcreate,Empupdate,Empdelete

urlpatterns = [
    path('',Emplist.as_view(),name="emplist"),
    path('create/',Empcreate.as_view(),name="empcreate"),
    path('update/<int:pk>',Empupdate.as_view(),name="empupdate"),
    path('delete/<int:pk>',Empdelete.as_view(),name="empdelete")
]