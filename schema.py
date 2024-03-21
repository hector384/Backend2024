import graphene
from eventos.schema import QueryEvents
from eventos.mutations import Mutation as EventMutations
from core.mutations import Mutation as CoreMutations
from escuelas.mutations import Mutation as SchoolMutation
from csrftoken.query import Query as CsrftokenQuery


class Query(QueryEvents, CsrftokenQuery, graphene.ObjectType):
    pass


class Mutation(EventMutations, SchoolMutation, CoreMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
