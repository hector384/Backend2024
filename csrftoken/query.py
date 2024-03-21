import graphene
from django.middleware.csrf import _get_new_csrf_string


class Query(graphene.ObjectType):
    token = graphene.String()

    def resolve_token(root, info):
        new_token = _get_new_csrf_string()
        print(new_token)
        return new_token
