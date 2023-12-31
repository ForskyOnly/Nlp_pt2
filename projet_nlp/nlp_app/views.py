from django.shortcuts import render, redirect
from .forms import SignUpForm, TexteForm, Patient, Psychologue
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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

@require_http_methods(['GET', 'POST'])
@login_required
def cree_patient(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        psychologue = request.user.psychologue
        
        patient = psychologue.cree_patient(first_name, last_name)
        
        return redirect('mes_patient')
    
    return render(request, 'psy.html')

@login_required
def mes_patient(request):
    query = request.GET.get('q', '')  
    
    psychologue = request.user.psychologue
    
    if query:
        patients = Patient.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(textes__content__icontains=query)
        ).prefetch_related('textes').distinct()
    else:
        patients = Patient.objects.filter(
            textes__content__icontains=query
        ).prefetch_related('textes').distinct()

    context = {
        'patients': patients,
        'query': query  
    }
    
    return render(request, 'mes_patient.html', context)



