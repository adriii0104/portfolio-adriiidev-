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




@app.errorhandler(500)
def internal_server_error(error):
    return 'Error interno del servidor. Por favor, contacta al administrador.', 500








"""----end----"""

if __name__ == '__main__':
    app.run(debug=True)




if BLOCK:
    print('App Blocked')
else:
    if __name__ == "__main__":
        app.run(debug=DEVELOPER_MODE)