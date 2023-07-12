from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Psychologue, Patient, Texte

class SignUpForm(UserCreationForm):
    is_psychologue = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'is_psychologue', )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = not self.cleaned_data.get('is_psychologue')
        user.is_psychologue = self.cleaned_data.get('is_psychologue')
        if commit:
            user.save()
            if user.is_psychologue:
                Psychologue.objects.create(user=user)
            else:
                Patient.objects.create(user=user)
        return user

class TexteForm(forms.ModelForm):
    class Meta:
        model = Texte
        fields = ['content']

