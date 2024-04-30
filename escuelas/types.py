import graphene


class GetSchoolType(graphene.ObjectType):
    school = graphene.String()
    route = graphene.String()
    id_picture = graphene.String()
    sizes = graphene.String()
    email = graphene.String()


class GetValidatorMailType(graphene.ObjectType):
    success = graphene.Boolean()
    message = graphene.String()
