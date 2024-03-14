from flask import *
from SITE.settings import *
from SITE.APIS.verapis import *
import time


app = Flask(__name__)
last_request = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            if 'file' in request.files:
                file = request.files['file']

                if file.filename != '':
                    results = SHOWFILES.upfiles(file.filename)
                    print(results)

            return redirect(url_for(request.endpoint))
    else:
            print(last_request)
            return render_template('index.html', files=SHOWFILES)
    
    
    
@app.route('/single', methods=['GET', 'POST'])
def single():
    try:
        ip=request.remote_addr
        if last_request.get(ip) == None:
            last_request[ip] = 0
        if request.method == 'POST':
            if last_request.get(ip) > 2:
                return redirect(url_for(request.endpoint))
            last_request[ip] +1
            endpoint = request.form.get('endpoint')
            method = request.form.get('method')
            requests = request.form.get('request')
            token = request.form.get('token')

            create = SHOWFILES.create_file(endpoint, method, token, requests)
            return redirect(url_for(request.endpoint))
        else:
            return render_template('single.html')
    except Exception as e:
        return redirect(url_for('internal_server_error'))




@app.errorhandler(500)
def internal_server_error(error):
    # Código para manejar el error interno del servidor
    return 'Internal Server Error', 500















@app.route("/api/datos", methods=['POST'])
def datos():
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









@app.route("/api/datose", methods=['POST'])
def datose():
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









@app.route("/api/datoselddll", methods=['POST'])
def datoselddll():
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









@app.route("/api/datoseldd", methods=['POST'])
def datoseldd():
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









@app.route("/api/datoseldddwds", methods=['POST'])
def datoseldddwds():
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









@app.route("/api/datoselddxx", methods=['POST'])
def datoselddxx():
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











"""----end----"""

if __name__ == '__main__':
    app.run(debug=True)




if BLOCK:
    print('App Blocked')
else:
    if __name__ == "__main__":
        app.run(debug=DEVELOPER_MODE)