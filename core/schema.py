# backend/core/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import ConfiguracionUsuario


class ConfiguracionUsuarioType(DjangoObjectType):
    class Meta:
        model = ConfiguracionUsuario


class Query(graphene.ObjectType):
    todos_tu_modelo = graphene.List(ConfiguracionUsuarioType)

    def resolve_todos_tu_modelo(self, info):
        return ConfiguracionUsuario.objects.all()


schema = graphene.Schema(query=Query)
