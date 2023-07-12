from django.shortcuts import render, redirect
from .forms import SignUpForm, TexteForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST

def home(request):
    return render(request, 'home.html')

class LoginView(LoginView):
    template_name = 'login.html'
    
class LogoutView(LogoutView):
    template_name = 'logout.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def patient_view(request):
    if request.method == 'POST':
        form = TexteForm(request.POST)
        if form.is_valid():
            texte = form.save(commit=False)
            texte.patient = request.user.patient
            texte.save()
            return redirect('home')
    else:
        form = TexteForm()
    return render(request, 'patient.html', {'form': form})