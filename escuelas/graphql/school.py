from backend.graphqlbase import baseGraphQL
from util.check import check
from django.core.validators import validate_email


class SchoolGraphql(baseGraphQL):

    def __init__(self, info):
        super().__init__(info)

    def RegisterSchool(self, **kwargs):

        check.check_name(kwargs["name"])
        validate_email(kwargs["email"])
        print(kwargs)
        return [True, "libardo123"]
