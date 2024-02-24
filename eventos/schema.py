import graphene
from .models import Evento
from .types import EventType


class QueryEvents:
    get_user = graphene.Field(EventType, username=graphene.String(required=True))
    all_user = graphene.List(EventType)

    def resolve_get_user(root, info, **kwargs):
        try:
            return Evento.objects.get(username=kwargs["username"])
        except:
            return None

    def resolve_all_user(root, info, **kwargs):
        return Evento.objects.all()
