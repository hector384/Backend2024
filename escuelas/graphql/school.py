from backend.graphqlbase import baseGraphQL


class SchoolGraphql(baseGraphQL):

    def __init__(self, info):
        super().__init__(info)

    def RegisterSchool(self, **kwargs):
        print(kwargs)
        return [True, "libardo123"]
