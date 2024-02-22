from django.shortcuts import render
from .schema import schema

from graphene_django.views import GraphQLView


class MyGraphQLView(GraphQLView):
    schema = schema


# Create your views here.
