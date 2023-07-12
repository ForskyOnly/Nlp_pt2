from django_elasticsearch_dsl import Document, fields, Date, Text
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.field import Keyword
from django_elasticsearch_dsl.registries import registry
from .models import Texte, Patient
from django.db import models

@registry.register_document
class TexteDocument(Document):
    date = models.DateField()

    class Index:
        name = 'textes'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    patient = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
    })

    class Django:
        model = Texte
        fields = ['emotion', 'content']

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Patient):
            return related_instance.texte_set.all()
