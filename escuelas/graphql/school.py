from backend.graphqlbase import baseGraphQL
from util.check import check
from django.core.validators import validate_email
from django.contrib.auth.models import User
from escuelas.models import School
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from util.images import ImageFormat
# from util.boto3 import conexionBoto
from util.boto3 import upload_file

class SchoolGraphql(baseGraphQL):

    def __init__(self, info):
        super().__init__(info)

    def RegisterUser(self, info, **kwargs):

        check.check_name(kwargs["first_name"])
        check.check_name(kwargs["last_name"])
        validate_email(kwargs["email"])
        check.check_password(kwargs['password'])
        check.check_username(kwargs['username'])
        
        #validar que no exista un usuario con ese mismo username
        search_user = User.objects.filter(username=kwargs['username'])
        if len(search_user) != 0:
            return { "success": False, "message": "Usuario ya existe!", "username": kwargs['username']}
        
        #validar que no exista un usuario con ese mismo email
        search_email = User.objects.filter(email=kwargs['email'])
        if len(search_email) != 0:
            return { "success": False, "message": "Email ya existe!", "username": kwargs['username']}
        
        """ if kwargs.get('picture') is not None:
            ImageFormat(kwargs['picture'], 1)
            upload_file(kwargs['picture'][0], kwargs['username']) """

        
        new_user = User()
        new_user.username = kwargs['username']
        new_user.email = kwargs['email']
        new_user.password = make_password(kwargs['password'])
        new_user.date_joined = datetime.now()
        new_user.first_name = kwargs['first_name']
        new_user.is_staff = False
        new_user.is_superuser = False
        new_user.is_active = False
        new_user.save()
        return { "success": True, "message": "", "username": kwargs['username']}
