import graphene
from graphene_django.debug import DjangoDebug
import compounds.schema


class Query(compounds.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
