# backend/core/urls.py
from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    # Otras URL específicas de la aplicación...
]