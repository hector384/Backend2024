
import graphene
from .types import GetSchoolType, GetValidatorMailType
from util.check import check
from .graphql.school import SchoolGraphql


class Query(graphene.ObjectType):

    get_schools = graphene.Field(
        GetSchoolType,
        title=graphene.String(required=False),
        sport=graphene.String(required=False),
        city=graphene.String(required=False),
        email=graphene.String(required=False),

        description="""Query para obtener la informacion de la escuela, session_key no es requerido""")
    get_exists = graphene.Field(
        GetValidatorMailType,
        cod=graphene.Int(required=True),
        data=graphene.String(required=True)
    )

    def resolve_get_schools(root, info, **kwargs):
        """Query para obtener la informacion de la escuela"""
        print("hoal"+info)
        p = SchoolGraphql(info).GetSchools(**kwargs)
        return p

    def resolve_get_exists(self, info, **kwargs):
        response = SchoolGraphql(info).ValidateUserEmail(**kwargs)
        return { "success": response["success"], "message": response['message']}
        # Llama a la función ValidateEmail para verificar si el correo está disponible
