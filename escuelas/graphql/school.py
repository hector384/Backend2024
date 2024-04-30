from backend.graphqlbase import baseGraphQL
from django.contrib.auth.models import User
from util.check import check
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from escuelas.models import School


class SchoolGraphql(baseGraphQL):

    def __init__(self, info):
        super().__init__(info)

    def RegisterSchool(self, **kwargs):
        """logica para crear una escuela"""
        user = User()
        user.email = kwargs('email')
        print(user.__dict__())
        return [True, "libardo123"]

    def GetSchools(self, **kwargs):
        if kwargs.get('city') != None:
            search = School.objects.filter(city__contains=kwargs['city'])
            if search != None:
                print(search)
                print(len(search))
            else:
                print("No School")
            """logica para responder..."""
            print('hola query')
            return {
                "school": str(len(search)),
                "route": 'hola route',
                "id_picture": 'hola id_picture',
                "sizes": 'hola sizes',
                "email": 'hola email',
            }

    def ValidateEmail(self, value):
        if User.objects.filter(email=value).exists():
            return {"success": False, "message": 'Correo ya usado'}
        else:
            return {"success": True, "message": 'Correo disponible'}

    def ValidateUserEmail(self, **kwargs):
        success = True
        message = ""
        if kwargs['cod'] == 1:
            # hay que validar usuario
            # result = SchoolGraphql(info).ValidateEmail(value=value)
            p = check.check_name(kwargs["data"])
            print(p)

            if p['success'] == True:
                if check.check_validateuser(kwargs["data"]):
                    success = False
                    message = "user  already used"
                # Extrae los valores de "success" y "message" de la respuesta
            else:
                success = p['success']
                message = p['message']

        elif kwargs['cod'] == 2:
            try:
                if validate_email(kwargs['data']):
                    if check.check_validate_email(kwargs['data']):
                        success = False
                        message = "email already used"
            except ValidationError:
                success = False
                message = "invalid email"
        else:
            success = False
            message = "invalid code"

        return {"success": success, "message": message}
