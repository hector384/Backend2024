from graphene_django.types import DjangoObjectType
from .models import Evento, Asistencia

class EventoType(DjangoObjectType):
    class Meta:
        model = Evento

class AsistenciaType(DjangoObjectType):
    class Meta:
        model = Asistencia