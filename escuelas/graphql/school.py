from backend.graphqlbase import baseGraphQL
from util.check import check
from django.core.validators import validate_email
from django.contrib.auth.models import User
from escuelas.models import School
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.db.models import Q

class SchoolGraphql(baseGraphQL):

    def __init__(self, info):
        super().__init__(info)

    def RegisterUser(self, **kwargs):

        check.check_name(kwargs["first_name"])
        check.check_name(kwargs["last_name"])
        validate_email(kwargs["email"])
        check.check_password(kwargs['password'])
        check.check_username(kwargs['username'])
        search_user = User.objects.filter(Q(username=kwargs['username']) ^ Q(email=kwargs['email']))
        for user in search_user:
            print(user.username, user.email)
            
        #validar que no exista un usuario con ese mismo id
        if len(search_user) == 0:
            print('ok', search_user)
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
        else:
            print('ya existe!')
            return { "success": False, "message": "Usuario/Email ya existe!", "username": kwargs['username']}
