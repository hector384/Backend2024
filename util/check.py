from graphql import GraphQLError
import re
from backend.settings import LOCAL_REDIS

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
            raise GraphQLError("la longitud del nombre debe ser  menor a 100")
        else:
            # if self.check_bad_words(name):
            #     raise GraphQLError('CCN-001: No se puede escribir en el nombre {}'.format(name))
            # elif len(name) > 3 :
            if len(name) > 3:
                regex = r"^~?[a-zA-ZÀ-ÿ0-9\s\u00F1\u00D1]+$"
                result = re.match(regex, name)
                if result is None:
                    raise GraphQLError("Solo se permiten letras en el nombre")
                return True
            else:
                raise GraphQLError("Longitud de nombre incorrecta")
        
    @classmethod
    def check_password(cls, password):
        if len(password)  < 8 or len(password) > 30 :
            raise GraphQLError('La contraseña debe tener por lo menos 8 dígitos y no mas de 30 digitos')
        number =(bool(re.search(r'\d', password)))
        letra = (bool(re.search(r'[a-zA-Z]', password)))
        if number == False:
            raise GraphQLError('La contraseña debe contener al menos un numero')
        elif letra == False:
            raise GraphQLError('La contraseña debe contener al menos una letra')
        else: 
            return True
    
    @classmethod 
    def check_phone(self, prefix, phone_str, len_number):
        """
        Valida el numero ingresado con una expresion regular, Actualmente valido solo para colombia ,
        """
        if len(phone_str) == len_number : 
            phone = prefix + phone_str
            regex = r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$"
            result = re.match(regex, phone)
            if result is None:
                raise GraphQLError('Ingrese un numero de telefono valido')
            return True
        else:
            raise GraphQLError(f'El telefono debe contener {len_number} digitos')

    @classmethod 
    def check_username(self,username):
        """Valida la sintaxis del usuario, si todo es correcto retorna True"""
        if  len(username) > 20 or len(username) < 5:
            raise GraphQLError('la longitud de no es permitida debe estar entre 5 y 20 caracteres')
        else:
            if self.check_bad_words(username):
                raise GraphQLError('No se puede escribir en el username {}'.format(username))
            else:
                regex = r'^[a-z0-9]+[a-z\d._]+\Z$'
                result = re.match(regex, username)
                if result is None:
                    raise GraphQLError('El username debe empezar con letra minusculas, del resto de los campos solo se permiten letras minusculas, numeros, _ , . , no se permite espacios entre linea')
                return True

    @classmethod
    def check_bad_words(self,_word):
        """Devuelve un True si la palabra contiene una groseria
        """
        bad_words = LOCAL_REDIS.get('bad_words')
        if not bad_words:
            raise GraphQLError("redis no dispone de 'bad words' primero se debe ejecutar la mutacion SubirRedis")
        word = " {} ".format(_word).lower()
        bad_words = bad_words.decode('UTF-8')
        bad_words =  bad_words.split(',')
        if not word.isalpha():
            word = re.sub("\$", "s", word)
            word = re.sub("\s+", " , ", word)
            replaces = {"0":"o", "1":"i", "2":"z", "3":"e", "4":"a", "5":"s", "6":"g", "7":"t", "8":"b", "9":"g", "@":"a"}
            word = re.sub("|".join(replaces.keys()), lambda match:replaces[match.string[match.start():match.end()]], word)
        for item in bad_words:
            salida = word.__contains__(item)
            if salida:
                return item
        return False
