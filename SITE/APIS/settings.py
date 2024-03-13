ALLOWED_EXTENSIONS = ['.json', '.txt', '.pdf']

RTFLS = 'SITE/APIS/Files/'




def files_up(endpoint_create, endpoint, method):
    return f'''
@app.route("{endpoint_create}", methods=["{method}"])
def {endpoint}():
    try:
        pass
    except Exception as e:
        return jsonify('Ha ocurrido un error inesperado')
\n\n\n\n\n\n\n'''
