from .types import EventType, AsistenciaType
from .models import Evento, Asistencia
import graphene
from .models import Evento

from django.contrib.auth.hashers import make_password, check_password


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

class CrearEvento(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        fecha = graphene.DateTime(required=True)
        lugar = graphene.String(required=True)
        descripcion = graphene.String(required=True)

    evento = graphene.Field(EventType)

    @staticmethod
    def mutate(root, info, nombre, fecha, lugar, descripcion):
        evento = Evento(nombre=nombre, fecha=fecha,
                        lugar=lugar, descripcion=descripcion)
        evento.save()
        return CrearEvento(evento=evento)


class ConfirmarAsistencia(graphene.Mutation):
    class Arguments:
        usuario_id = graphene.ID(required=True)
        evento_id = graphene.ID(required=True)

    asistencia = graphene.Field(AsistenciaType)

    @staticmethod
    def mutate(root, info, usuario_id, evento_id):
        asistencia = Asistencia(usuario_id=usuario_id,
                                evento_id=evento_id, confirmado=True)
        asistencia.save()
        return ConfirmarAsistencia(asistencia=asistencia)


class Mutation(graphene.ObjectType):
    create_event = CrearEvento.Field()
    confirm_event_assist = ConfirmarAsistencia.Field()
