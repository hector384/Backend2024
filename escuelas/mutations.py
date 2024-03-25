import graphene
from .models import School
from graphene_file_upload.scalars import Upload
from escuelas.graphql.school import SchoolGraphql


class CreateSchool(graphene.Mutation):
    class Arguments:
        id_user = graphene.String(required=True)
        name = graphene.String(required=True)
        address = graphene.String()
        city = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        telephone = graphene.String(required=True)
        is_instructor = graphene.String()

    success = graphene.Boolean()
    id_user = graphene.String()

    @staticmethod
    def mutate(cls, info, **kwargs):
        register = SchoolGraphql(info).RegisterSchool(**kwargs)
        return CreateSchool(success=register['success'], id_user=register['id_user'])


class Mutation(graphene.ObjectType):
    school_register = CreateSchool.Field()
