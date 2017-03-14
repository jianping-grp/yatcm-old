from . import models
from graphene import AbstractType, Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class CompoundNode(DjangoObjectType):
    class Meta:
        model = models.Compound
        interfaces = (Node,)
        exclude_fields = [
            'mol',
            'bfp'
        ]
        filter_fields = [
            'english_name',
            'chinese_name',
        ]

    @classmethod
    def get_node(cls, id, context, info):
        try:
            cpd = cls._meta.model.objects.get(id=id)
        except cls._meta.model.DoesNotExist:
            return None
        return cpd


class HerbNode(DjangoObjectType):
    class Meta:
        model = models.Herb
        interfaces = (Node,)


class PrescriptionNode(DjangoObjectType):
    class Meta:
        model = models.Prescription
        interfaces = (Node,)


class KEGGPathwayNode(DjangoObjectType):
    class Meta:
        model = models.KEGGPathway
        interfaces = (Node,)


class Query(AbstractType):
    compound = Node.Field(CompoundNode)
    all_compound = DjangoFilterConnectionField(CompoundNode)

    herb = Node.Field(HerbNode)
    all_herb = DjangoFilterConnectionField(HerbNode)

    prescription = Node.Field(PrescriptionNode)
    all_prescription = DjangoFilterConnectionField(PrescriptionNode)

    keggpathway = Node.Field(KEGGPathwayNode)
    all_keggpathway = DjangoFilterConnectionField(KEGGPathwayNode)