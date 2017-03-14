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


class Query(AbstractType):
    compound = Node.Field(CompoundNode)
    all_compound = DjangoFilterConnectionField(CompoundNode)
