from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from .models import Task
from .forms import TaskForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm

class Home(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return Task.objects.filret(user=self.request.user)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'deadline']
    template_name = 'tasks/update_task.html'
    success_url = '/'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = '/'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    
    
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    error = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user=user)
            return redirect('home')
        else:
            error = 'Неверный логин или пароль'
    
    return render(request, 'tasks/login.html')
            
            
def user_logout(request):
    logout(request)
    return redirect('login')


class Register(View):
    
    template_name = 'tasks/register.html'
    
    def get(self, request):
        context = {
            'form': UserRegisterForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(request, username=username, password=password)
            login(request, user)
            
            return redirect('home')
        
        return render(request, self.template_name, {'form': form})
