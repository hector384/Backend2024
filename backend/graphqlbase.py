from util.token import get_csrftoken_by_request
from datetime import datetime
from uuid import uuid1


class baseGraphQL:

    QUERY = "Query"
    MUTATION = "Mutation"
    SUSCRIPTION = "Suscription"
    FUNCTION = "Function"

    def __init__(self, info):
        self.info = info
        self.headers = self.info.context.META
        self.token = get_csrftoken_by_request(self.info)
        self.timestamp = datetime.today()
        self.timeuuid = uuid1()

    def get_uuid1(self):
        return uuid1()

    # def login_required(self,info,session):
    #     """Recibe Info , session_key   si la session es correcta retorna el Username, si es incorrecta o no exite
    #     genera un GraphQLError
    #     """
    #     check.check_session_key(session)
    #     ses = Session.objects.values_list('username','csrftoken').filter(session_key=session)
    #     if len(ses)==1:
    #         if self.getGeneralUserBlock(ses[0][0]):
    #             self.deleteAllUserSessions(ses[0][0])
    #             raise GraphQLError('Usuario bloqueado por Tz')
    #         if self.token == ses[0][1] :
    #             user = User.objects.filter(username=ses[0][0])
    #             """ if user[0].id_city == ' ':
    #                 raise GraphQLError('El usuario debe tener una ciudad') """
    #             if len(user) == 1 and user[0].activate == True :
    #                 self.user_login = user[0]
    #                 return user[0]
    #             else:
    #                 raise GraphQLError('Existe un error con el usuario')
    #         else:
    #             raise GraphQLError('Acceso denegado')
    #     else:
    #         raise GraphQLError('La session no existe')

    # def searchUser(self, info , **kwargs):
    #     #funcion encontrar si existe session_key en kwargs y encontrar registro en User
    #     user = False
    #     if kwargs.get('session_key')!= None and kwargs.get('session_key') != '*':
    #         user = self.login_required(info, kwargs['session_key'])
    #     return user

    # def deleteAllUserSessions(self,id_user):
    #     """Elimina todas las sessiones del usuario de las tablas correspondientes"""
    #     sessions_by_user = SessionByUser.objects.filter(username = id_user)
    #     list_sessions =[]
    #     list_csrftoken =[]
    #     for session in sessions_by_user:
    #         list_sessions.append(session.session_key)
    #         list_csrftoken.append(session.csrftoken)
    #     Session.objects.filter(session_key__in=list_sessions).delete()
    #     SessionByCsrftoken.objects.filter(csrftoken__in=list_csrftoken).delete()
    #     sessions_by_user.delete()
    #     User.objects.filter(username=id_user).update(total_sessions=0)
    #     try:
    #         changeGeneralStatistics('login_users', -len(list_sessions))
    #     except:
    #         self.save_programing_error(
    #             2,
    #             self.FUNCTION,
    #             'services_get_payment_gateways_of_a_store',
    #             'Error de consistencia: no se almacena datos de estadisticas para el modelo GeneralStatistics, login_users',
    #         )
    #     return True
