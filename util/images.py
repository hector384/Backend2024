from graphql import GraphQLError
def ImageFormat(image, cant):
    #funcion para validar el formato de la imagen y su cantidad máxima
    if len(image)>cant:
        raise GraphQLError('Supera el limite de imagenes, solo se puede {} como máximo'.format(cant))
    elif len(image)== 0:
        raise GraphQLError('Debe seleccionar una imagen')
    for item in image:
        j = str(item).lower()
        if j.endswith('.jpg') == False and j.endswith('.jpeg')==False:
            raise GraphQLError('{} no es un archivo .jpg o .jpeg'.format(str(item)))
    return