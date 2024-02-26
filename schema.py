import graphene
import eventos.schema
from eventos.mutations import Mutation as EventMutations
from core.mutations import Mutation as CoreMutations


class Query(eventos.schema.QueryEvents, graphene.ObjectType):
    pass


class Mutation(EventMutations, CoreMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
