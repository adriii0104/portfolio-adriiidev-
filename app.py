from flask import *
from SITE.settings import *
from SITE.APIS.verapis import *
import time
from SITE.MESSAGES.sendmail import *
from SITE.MESSAGES.Codes import *
from SITE.MESSAGES.auth import *



app = Flask(__name__)
app.secret_key= 'cogiteunairecomoquetehicientenienteslfmad;lgnasdklfn'
last_request = {}
verify_users = {}

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
        # aqui obtenemos la dirección IP del usuario para hacer algunas validaciones.
        ip=request.remote_addr
        
        
        if last_request.get(ip) == None:
            last_request[ip] = 0
        if request.method == 'POST':
            if last_request.get(ip) > 4:
                return redirect(url_for(request.endpoint))
            
            if request.form.get('email'):
                email = request.form.get('email')
                code = GeneradorDeCodigos().intcode()
                
                response = authuser(email, code)
                
                if response:
                    last_request[ip] + 1
                
                    MAIL().enviar_correo(email, 'Código de verificación', f'Su código de verificación es: {code}')
                    
                    session['email'] = email
                    

                    return redirect(url_for(request.endpoint))
                else:
                    return redirect(url_for('internal_server_error'))
            
            codigo = request.form.get('codigo')
            
            if codigo:  
                last_request[ip] +1
                endpoint = request.form.get('endpoint')
                method = request.form.get('method')
                requests = request.form.get('request')
                token = request.form.get('token')
                create = SHOWFILES.create_file(endpoint, method, token, requests)
                return redirect(url_for(request.endpoint))
            else:
                return redirect(url_for(request.endpoint), flash('Código incorrecto'))
        else:
            return render_template('single.html', access=False if 'email' not in session else True, code=False if 'email' not in session else True)
    except Exception as e:
        print('error',e)


@app.route('/clearsession', methods=['GET'])
def closesession():
    session.clear()
    return redirect(url_for('single'))  # Corregido el uso de url_for

@app.errorhandler(500)
def internal_server_error(error):
    # Código para manejar el error interno del servidor
    return 'Internal Server Error', 500




















"""----end----"""

if __name__ == '__main__':
    app.run(debug=True)




if BLOCK:
    print('App Blocked')
else:
    if __name__ == "__main__":
        app.run(debug=DEVELOPER_MODE)