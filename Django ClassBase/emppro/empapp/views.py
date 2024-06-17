from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Emp

# Create your views here.

class Emplist(ListView):
    model = Emp
    template_name = "emplist.html"
    context_object_name = "emps"
    
class Empcreate(CreateView):
    model = Emp
    fields = "__all__"
    template_name = "empcreate.html"
    success_url = reverse_lazy("emplist")
    
class Empupdate(UpdateView):
    model = Emp
    fields = "__all__"
    template_name = "empupdate.html"
    success_url = reverse_lazy("emplist")
    
class Empdelete(DeleteView):
    model = Emp
    template_name = "empdelete.html"
    success_url = reverse_lazy("emplist")