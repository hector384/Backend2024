import graphene
from graphene_django.types import DjangoObjectType
from .models import Evento, Asistencia

class EventoType(DjangoObjectType):
    class Meta:
        model = Evento

class AsistenciaType(DjangoObjectType):
    class Meta:
        model = Asistencia

class CrearEvento(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        fecha = graphene.DateTime(required=True)
        lugar = graphene.String(required=True)
        descripcion = graphene.String(required=True)

    evento = graphene.Field(EventoType)

    @staticmethod
    def mutate(root, info, nombre, fecha, lugar, descripcion):
        evento = Evento(nombre=nombre, fecha=fecha, lugar=lugar, descripcion=descripcion)
        evento.save()
        return CrearEvento(evento=evento)

class ConfirmarAsistencia(graphene.Mutation):
    class Arguments:
        usuario_id = graphene.ID(required=True)
        evento_id = graphene.ID(required=True)

    asistencia = graphene.Field(AsistenciaType)

    @staticmethod
    def mutate(root, info, usuario_id, evento_id):
        asistencia = Asistencia(usuario_id=usuario_id, evento_id=evento_id, confirmado=True)
        asistencia.save()
        return ConfirmarAsistencia(asistencia=asistencia)

class Mutaciones(graphene.ObjectType):
    crear_evento = CrearEvento.Field()
    confirmar_asistencia = ConfirmarAsistencia.Field()

class Query(graphene.ObjectType):
    ...

schema = graphene.Schema(query=Query, mutation=Mutaciones)
