from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import Sistemas_Reglas.principal as sr

app = Flask(__name__)
CORS(app)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'Admin'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
mysql = MySQL(app)

# settings A partir de ese momento Flask utilizará esta clave para poder cifrar la información de la cookie
app.secret_key = "mysecretkey"

@app.route('/getSistemaReglas/<v_repiratorio>/<v_fatiga>/<v_dolor>/<v_cuello>/<v_debiliad>', methods=['GET'])
def getSistemaReglas(v_repiratorio, v_fatiga, v_dolor, v_cuello, v_debiliad):
    sr.preguntas(v_repiratorio, v_fatiga, v_dolor, v_cuello, v_debiliad)



# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)