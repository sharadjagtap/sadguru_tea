from django.shortcuts import render
# Create your views here.
from testapp.models import Tea
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse

class TeaList_view(ListView):
    model = Tea

class TeaDetail_view(DetailView):
    model = Tea

class Teacreateview(CreateView):
    model = Tea
    fields = '__all__'

class UpdateTea(UpdateView):
    model = Tea
    fields = ['name','price']

class Tea_Delete_view(DeleteView):
    model = Tea
    success_url =reverse_lazy('home')