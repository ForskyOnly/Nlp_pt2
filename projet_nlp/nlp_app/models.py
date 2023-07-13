from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.utils.crypto import get_random_string

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set")

    is_patient = models.BooleanField(default=False)
    is_psychologue = models.BooleanField(default=False)

class Psychologue(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='psychologue')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    
    def cree_patient(self, first_name, last_name):
        password = get_random_string(length=8)
        
        user = User.objects.create_user(
            username=f"{first_name}.{last_name}",
            password=password,
        )
        
        patient = Patient.objects.create(
            user=user,
            psychologue=self,
            first_name=first_name,
            last_name=last_name,
        )
        
        return patient

class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient')
    psychologue = models.ForeignKey(Psychologue, on_delete=models.SET_NULL, null=True, related_name='patients')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

class Texte(models.Model):
    content = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='textes')
    emotion = models.CharField(max_length=200, blank=True, null=True) 
    date = models.DateTimeField(auto_now_add=True)

