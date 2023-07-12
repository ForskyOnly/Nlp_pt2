from django.shortcuts import render, redirect
from .forms import SignUpForm, TexteForm
from django.contrib.auth.views import LoginView, LogoutView

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
            user = form.save(commit=False)  # Obtenir l'instance du modèle sans l'enregistrer en base de données

            if form.cleaned_data['is_psychologue']:
                user.is_psychologue = True
                user.is_patient = False
            else:
                user.is_psychologue = False
                user.is_patient = True

            user.save()  # Enregistrer l'utilisateur en base de données

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

    