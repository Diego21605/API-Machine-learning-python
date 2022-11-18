from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import sys
sys.path.append('C:/Users/Diego Fernandez/Documents/GitHub/Api-Python/Api-Ptyhon/Sistemas_Reglas')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Mysql Connection¿
app.config['MYSQL_HOST'] = 'finalproject.csl9lso2teho.us-east-1.rds.amazonaws.com' 
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'dbFinalProject'
mysql = MySQL(app)

@app.route('/get/<v_repiratorio>/<v_fatiga>/<v_dolor>/<v_cuello>/<v_debiliad>', methods=['GET'])
def postSistemaReglas(v_repiratorio, v_fatiga, v_dolor, v_cuello, v_debiliad):    
    try:
        datos = sys.preguntas(v_repiratorio, v_fatiga, v_dolor, v_cuello, v_debiliad)
        # cur = mysql.connection.cursor()
        # cur.execute('SELECT * FROM Prueba WHERE Nuevo2 = %s', (v))
        # rv = cur.fetchall()
        # cur.close()
        # payload = []
        # content = {}
        # for result in rv:
        #     content = {'Nuevo': result[0], 'Nuevo2': result[1]}
        #     payload.append(content)
        #     content = {}
        # return jsonify(payload)
        return datos
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/getUsuario/<id>/<password>', methods=['GET'])
def getUsuario(id, password):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Usuario WHERE Id = %s AND Contrasena = %d', (id,password))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id': result[0], 'Nombre': result[1]}
            payload.append(content)
            content = {}
        return jsonify(payload)
        return datos
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})



@app.route('/postSistemaReglas', methods=['POST'])
def add_contact():
    try:
        if request.method == 'POST':
            return jsonify({"informacion":"Registro exitoso"})        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)