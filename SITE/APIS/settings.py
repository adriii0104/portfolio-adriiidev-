ALLOWED_EXTENSIONS = ['.json', '.txt', '.pdf']

RTFLS = 'SITE/APIS/Files/'



def files_up(endpoint_create, endpoint, method):
    """
    Esta función genera código para definir una ruta en una aplicación Flask
    para subir archivos.

    Args:
        endpoint_create (str): El endpoint de la ruta.
        endpoint (str): El nombre de la función de la vista.
        method (str): El método HTTP permitido para la ruta (por ejemplo, 'POST').

    Returns:
        str: El código Python para definir la ruta.
    """
    return f'''
@app.route("{endpoint_create}", methods=['{method}'])
def {endpoint}():
    try:
        # Verificar si la solicitud es POST
        if request.method == 'POST':
            # Obtener el archivo enviado en la solicitud
            file = request.files['file']
            filename = file.filename
            # Verificar si se ha enviado un archivo
            if filename != '':
                # Verificar si el archivo ya existe en la carpeta de archivos
                results = SHOWFILES.upfiles(filename)
                if results[0]:
                    # Guardar el archivo en la carpeta de archivos si no existe
                    file.save(os.path.join(RTFLS, filename))
                    return jsonify(results[1])  # Devolver resultado exitoso
                else:
                    # Devolver un mensaje de error si el archivo ya existe
                    return jsonify(results[1])
            else:
                # Devolver un mensaje si no se ha subido ningun archivo
                return jsonify('No se ha subido ningun archivo')
    except Exception as e:
        # Devolver un mensaje si ocurre un error inesperado
        return jsonify('Ha ocurrido un error inesperado')
\n\n\n\n\n\n\n\n\n'''
