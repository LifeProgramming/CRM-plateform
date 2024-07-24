from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Record
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import login, logout
from .forms import RegisterForm, RecordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class records(LoginRequiredMixin,ListView):
    model= Record
    context_object_name='records'
    template_name='capp/records.html'
    paginate_by=10

    def get_queryset(self):
        queryset = Record.objects.filter(creator=self.request.user)
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context

class record(LoginRequiredMixin,DetailView):
    model=Record
    context_object_name='record'
    template_name='capp/record.html'

class loginUser(FormView):
    form_class = AuthenticationForm
    template_name = 'capp/login.html' 

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "This user does not exist!")
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse('Sorry! You have already logged in!')
        return super().get(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('records')
    
def logoutUser(request):
    logout(request)
    return redirect('records')

class rgisterUser(CreateView):
    form_class=RegisterForm
    template_name='capp/signup.html'
    success_url=reverse_lazy('records')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def form_invalid(self, form):
        messages.info(self.request, "Sorry! Something went wrong!!!")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        kwargs['form'] = self.form_class()
        return super().get_context_data(**kwargs)
    
class recordCreation(LoginRequiredMixin,CreateView):
    form_class=RecordForm
    template_name='capp/recordForm.html'
    success_url=reverse_lazy('records')

    def form_valid(self, form):
        form.instance.creator=self.request.user
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        messages.info(self.request, "Sorry! Something went wrong!!!")
        return super().form_invalid(form)

@login_required(login_url='login')
def updateRecord(request, pk):
    record= Record.objects.get(id=pk)
    form=RecordForm(request.POST or None, instance=record)
    user=request.user
    if record.creator!=user:
        return HttpResponseForbidden('Sorry! You are not allowed to change this record!')
    if request.method=='POST':
        form=RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('records')
        
    return render(request,'capp/recordForm.html',{'form':form})

@login_required(login_url='login')
def deleteRecord(request,pk):
    record=Record.objects.get(id=pk)
    record.delete()
    return redirect('records')