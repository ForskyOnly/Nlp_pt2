from django.core.management.base import BaseCommand
from faker import Faker

from nlp_app.models import Psychologue, Patient, User

class Command(BaseCommand):
    help = 'Generates random users, psychologists, and patients'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(5):
            user = User.objects.create_user(username=fake.user_name(), password=fake.password(), is_psychologue=True)
            Psychologue.objects.create(user=user, first_name=fake.first_name(), last_name=fake.last_name())

        all_psychologists = Psychologue.objects.all()

        for i in range(50):
            user = User.objects.create_user(username=fake.user_name(), password="Azerty@123", is_patient=True)
            patient = Patient.objects.create(user=user, first_name=fake.first_name(), last_name=fake.last_name())
            patient.psychologue = all_psychologists[i % 5]  
            patient.save()
