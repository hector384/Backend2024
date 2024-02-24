import graphene
from graphene_django.types import DjangoObjectType
from .models import Sitio
from .models import ConfiguracionUsuario


class ConfiguracionUsuarioType(DjangoObjectType):
    class Meta:
        model = ConfiguracionUsuario
        
class SitioType(DjangoObjectType):
    class Meta:
        model = Sitio
