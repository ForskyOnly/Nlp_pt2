from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set")

    is_patient = models.BooleanField(default=False)
    is_psychologue = models.BooleanField(default=False)

class Psychologue(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='psychologue')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient')
    psychologue = models.ForeignKey(Psychologue, on_delete=models.SET_NULL, null=True, related_name='patients')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

class Texte(models.Model):
    content = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    emotions = models.CharField(max_length=200, blank=True, null=True) 
    date = models.DateTimeField(auto_now_add=True)
