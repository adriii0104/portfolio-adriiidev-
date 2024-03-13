from flask import *
from SITE.settings import *
from SITE.APIS.verapis import *


app = Flask(__name__)


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
        return render_template('index.html', files=SHOWFILES)
    
    
    
@app.route('/single', methods=['GET', 'POST'])
def single():
    if request.method == 'POST':
        endpoint = request.form.get('endpoint')
        method = request.form.get('method')
        requests = request.form.get('request')
        token = request.form.get('token')
        print(requests)
        
        create = SHOWFILES.create_file(endpoint, method, token, requests)
        return redirect(url_for(request.endpoint))
    else:
        return render_template('single.html')




@app.errorhandler(500)
def internal_server_error(error):
    return 'Error interno del servidor. Por favor, contacta al administrador.', 500








@app.route("/api/datasdse", methods=["POST"])
def datasdse():
    try:
        pass
    except Exception as e:
        return jsonify('Ha ocurrido un error inesperado')







@app.route("/api/aadatasdse", methods=["POST"])
def aadatasdse():
    try:
        pass
    except Exception as e:
        return jsonify('Ha ocurrido un error inesperado')







@app.route("/api/datosesaddd", methods=["POST"])
def datosesaddd():
    try:
        pass
    except Exception as e:
        return jsonify('Ha ocurrido un error inesperado')







@app.route("/api/datoseldcadsas", methods=["POST"])
def datoseldcadsas():
    try:
        pass
    except Exception as e:
        return jsonify('Ha ocurrido un error inesperado')









"""----end----"""

if __name__ == '__main__':
    app.run(debug=True)




if BLOCK:
    print('App Blocked')
else:
    if __name__ == "__main__":
        app.run(debug=DEVELOPER_MODE)