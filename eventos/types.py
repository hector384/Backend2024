from graphene_django import DjangoObjectType
from .models import Evento


class EventType(DjangoObjectType):
    class Meta:
        model = Evento
        fields = "__all__"
