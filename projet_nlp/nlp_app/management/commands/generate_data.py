from django.core.management.base import BaseCommand
from faker import Faker

from nlp_app.models import Psychologue, Patient, User

class Command(BaseCommand):
    help = 'Generates random users, psychologists, and patients'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create one psychologist
        user = User.objects.create_user(username="Le_Psy", password="Lepsy@59800", is_psychologue=True)
        psychologue = Psychologue.objects.create(user=user, first_name=fake.first_name(), last_name=fake.last_name())

        # Create 10 patients and assign them to the created psychologist
        for _ in range(10):
            user = User.objects.create_user(username=fake.user_name(), password="Azerty@123", is_patient=True)
            patient = Patient.objects.create(user=user, first_name=fake.first_name(), last_name=fake.last_name())
            patient.psychologue = psychologue
            patient.save()
