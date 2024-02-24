import graphene
from .models import Evento


class CreateEvent(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)

    success = graphene.Boolean()
    username = graphene.String()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
            events = Evento.objects.values_list().all()
            print(events, "holamundo")
            return CreateEvent(success=True, username=kwargs["username"])
        except:
            print("error")
            return CreateEvent(success=False, username=kwargs["username"])


class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
