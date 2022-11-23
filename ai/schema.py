import graphene
from graphene_django import DjangoObjectType
#from users.schema import UserType

#from .models import Link


#class LinkType(DjangoObjectType):
#    class Meta:
#        model = Link


class Query(graphene.ObjectType):
    linear = graphene.String(value=graphene.String())

    class Arguments:
        value = graphene.String()

    def resolve_linear(self, info, value,  **kwargs):
        return "100.23"


