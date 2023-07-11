from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Texte, Patient

@registry.register_document
class TexteDocument(Document):
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
        fields = [
            'date',
            'emotions',
            'content',
        ]


    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Patient):
            return related_instance.texte_set.all()
