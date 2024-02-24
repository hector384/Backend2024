import graphene
import eventos.schema
from eventos.mutations import Mutation as EventMutations


class Query(
    eventos.schema.QueryEvents,

        graphene.ObjectType):
    pass


class Mutation(EventMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
