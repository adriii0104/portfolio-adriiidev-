#aqui vamos a convertir todos tipos de archivos al que el usuario pida, el que el usuario suba al que el pida.
import os
from PIL import Image

class File_Converter:
    def __init__(self) -> None:
        self.ALLOWED_EXTENSIONS_IMAGE = ['.png', '.jpg', '.avif']
    
    
    def converter_pic(self, file:str, to:str) -> str:
            try:
                name, ext = os.path.splitext(file)
                if ext.lower() not in self.ALLOWED_EXTENSIONS:
                    return 'El archivo no es permitido.'
                else:
                    if to.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
                        img = Image.open(file)
                        img.save(name + to)
                        return name + to, 'Archivo convertido con éxito.'
                    else:
                        return 'El formato de salida no es permitido.'
            except Exception as e:
                return f'Error al convertir el archivo: {e}'



file = File_Converter()

file.converter_pic('image.png', '.jpg')