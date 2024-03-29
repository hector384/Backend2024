import graphene
from .models import School
from graphene_file_upload.scalars import Upload
from escuelas.graphql.school import SchoolGraphql


class RegisterUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    success = graphene.Boolean()
    username = graphene.String()
    message = graphene.String()

    @staticmethod
    def mutate(cls, info, **kwargs):
        register = SchoolGraphql(info).RegisterUser(**kwargs)
        return RegisterUser(success=register['success'], username=register['username'], message=register['message'])


class Mutation(graphene.ObjectType):
    user_register = RegisterUser.Field()
