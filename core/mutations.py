from core.types import ConfiguracionUsuarioType, SitioType
import graphene
from .models import Sitio
from .models import ConfiguracionUsuario


class CrearConfiguracionUsuario(graphene.Mutation):
    class Arguments:
        usuario_id = graphene.ID(required=True)
        avatar = graphene.String()
        fecha_nacimiento = graphene.String()
        bio = graphene.String()
        sitio_web = graphene.String()

    configuracion_usuario = graphene.Field(ConfiguracionUsuarioType)

    @staticmethod
    def mutate(root, info, usuario_id, avatar=None, fecha_nacimiento=None, bio=None, sitio_web=None):
        configuracion_usuario = ConfiguracionUsuario.objects.create(
            usuario_id=usuario_id,
            avatar=avatar,
            fecha_nacimiento=fecha_nacimiento,
            bio=bio,
            sitio_web=sitio_web
        )
        return CrearConfiguracionUsuario(configuracion_usuario=configuracion_usuario)


class ActualizarConfiguracionUsuario(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        avatar = graphene.String()
        fecha_nacimiento = graphene.String()
        bio = graphene.String()
        sitio_web = graphene.String()

    configuracion_usuario = graphene.Field(ConfiguracionUsuarioType)

    @staticmethod
    def mutate(root, info, id, avatar=None, fecha_nacimiento=None, bio=None, sitio_web=None):
        configuracion_usuario = ConfiguracionUsuario.objects.get(pk=id)
        if avatar is not None:
            configuracion_usuario.avatar = avatar
        if fecha_nacimiento is not None:
            configuracion_usuario.fecha_nacimiento = fecha_nacimiento
        if bio is not None:
            configuracion_usuario.bio = bio
        if sitio_web is not None:
            configuracion_usuario.sitio_web = sitio_web
        configuracion_usuario.save()
        return ActualizarConfiguracionUsuario(configuracion_usuario=configuracion_usuario)


class EliminarConfiguracionUsuario(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        configuracion_usuario = ConfiguracionUsuario.objects.get(pk=id)
        if configuracion_usuario != None:
            configuracion_usuario.delete()
            success = True
        else:
            success = False

        return EliminarConfiguracionUsuario(success=success)


class CrearSitio(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        slogan = graphene.String()
        descripcion = graphene.String()
        logo = graphene.String()

    sitio = graphene.Field(SitioType)

    @staticmethod
    def mutate(root, info, nombre, slogan=None, descripcion=None, logo=None):
        sitio = Sitio(nombre=nombre, slogan=slogan,
                      descripcion=descripcion, logo=logo)
        sitio.save()
        return CrearSitio(sitio=sitio)


class ActualizarSitio(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String()
        slogan = graphene.String()
        descripcion = graphene.String()
        logo = graphene.String()

    sitio = graphene.Field(SitioType)

    @staticmethod
    def mutate(root, info, id, nombre=None, slogan=None, descripcion=None, logo=None):
        sitio = Sitio.objects.get(pk=id)
        if nombre is not None:
            sitio.nombre = nombre
        if slogan is not None:
            sitio.slogan = slogan
        if descripcion is not None:
            sitio.descripcion = descripcion
        if logo is not None:
            sitio.logo = logo
        sitio.save()
        return ActualizarSitio(sitio=sitio)


class EliminarSitio(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        sitio = Sitio.objects.get(pk=id)
        sitio.delete()
        return EliminarSitio(ok=True)

class Mutation(graphene.ObjectType):
    create_configuration_user = CrearConfiguracionUsuario.Field()
    update_configuration_user = ActualizarConfiguracionUsuario.Field()
    delete_configuration_user = EliminarConfiguracionUsuario.Field()
