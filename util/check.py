from graphql import GraphQLError


class check:
    def __init__(self, funcion, parametro):
        self.switch(funcion, parametro)

    def switch(self, funcion, parametro):
        f = getattr(self, funcion)
        f(parametro)

    @classmethod
    def check_csrftoken(self, csrftoken):
        """Devuelve True si la longitud del token es correcta"""
        if csrftoken != None and len(csrftoken) == 64 and csrftoken.isalnum():
            return True
        else:
            raise GraphQLError("Token invalido")
