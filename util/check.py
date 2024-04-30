from graphql import GraphQLError
from django.contrib.auth.models import User
import re


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

    @classmethod
    def check_name(self, name):
        """valida :
        - Longitud menor a 100 Caracteres
        - Solo permite letras y espacios
        """
        len_name = len(name)
        if len_name > 100:
            raise GraphQLError(
                "la longitud del nombre debe ser  menor a 100")  # U_001
        else:
            # if self.check_bad_words(name):
            #     raise GraphQLError('CCN-001: No se puede escribir en el nombre {}'.format(name))
            # elif len(name) > 3 :
            if len(name) > 3:
                regex = r'^~?[a-zA-ZÀ-ÿ\s\u00F1\u00D1]+$'
                result = re.match(regex, name)
                if result is None:
                    message = "Solo se permiten letras en el nombre"
                    success = False
                    return {"success": success, "message": message}
                    # return  GraphQLError("Solo se permiten letras en el nombre")
                return {"success": True, "message": "ola k axe"}
            else:
                raise GraphQLError("Longitud de nombre incorrecta")

    @classmethod
    def check_validateuser(self, data):
        return User.objects.filter(username=data).exists()

    @classmethod
    def check_validate_email(self, value):
        return User.objects.filter(email=value).exists()
