from backend.graphqlbase import baseGraphQL
from util.check import check
from django.core.validators import validate_email


class SchoolGraphql(baseGraphQL):

    def __init__(self, info):
        super().__init__(info)

    def RegisterSchool(self, **kwargs):

        check.check_name(kwargs["name"])
        validate_email(kwargs["email"])
        check.check_password(kwargs['password'])
        check.check_phone("+57", kwargs['telephone'], 10)
        check.check_username(kwargs['id_user'])
        return { "success": True, "id_user": kwargs['name']}
