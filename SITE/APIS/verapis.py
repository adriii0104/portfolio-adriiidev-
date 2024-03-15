import os
import sys
from SITE.APIS.settings import *

class SHOWFILES:
    @staticmethod
    def __init__():pass


    @staticmethod
    def listfiles() -> list:
        first_route = 'SITE/APIS/Files'

        Files = os.listdir(first_route)

        return Files
    

    @staticmethod
    def showfile(file: str):
        name, ext = os.path.splitext(file)

        route = RTFLS+file

        if ext.lower() not in ALLOWED_EXTENSIONS:
            return 'Error', 'El archivo no es permitido.'
        else:
            with open(route, 'r', encoding='utf-8') as read:
                return read.readlines()
            
    @staticmethod
    def upfiles(file:str):
        try:
            _, ext = os.path.splitext(file)

            if ext.lower() not in ALLOWED_EXTENSIONS:
                return False, 'El archivo no es permitido.'
            name_file = os.path.join(RTFLS, file)
            if os.path.exists(name_file):
                return False, 'El Archivo ya existe, desea cambie el nombre y vuelva a subirlo.'
            
            return True, 'Archivo cargado con éxito'
        except Exception as Error:
            return False, 'Ha ocurrido un error inesperado'
        
    @staticmethod
    def create_file(endpoint:str, method:str, auth:bool, requests:str) -> bool:
        
        if method not in ['POST', 'PUT', 'DELETE']:
            print('El método no es permitido')
            return False, 'El método no es permitido'
        with open('app.py', 'r') as file_path:
            data = file_path.readlines()
            for i in range(len(data)):
                if data[i].find('def '+endpoint+'(') != -1:
                    print('El endpoint ya existe')
                    return False, 'El endpoint ya existe'
                else:
                    #aqui se supone que debo de agregar el endpoint con las especificaciones del usuario.
                    if data[i].find('----end----') != -1:
                        
                        endpoint_create = '/api/'+endpoint
                        
                        data[i - 3] = files_up(endpoint_create, endpoint, method) if requests == 'up&down' else '\n'
                        
                        with open('app.py', 'w') as file_path:
                            file_path.writelines(data)
                        return True
            return False