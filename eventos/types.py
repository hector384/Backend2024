from graphene_django import DjangoObjectType
from .models import Asistencia, Evento


class EventType(DjangoObjectType):
    class Meta:
        model = Evento
        fields = "__all__"


class AsistenciaType(DjangoObjectType):
    class Meta:
        model = Asistencia
        fields = "__all__"
