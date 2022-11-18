from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import pandas as pd
import RandomForestPredict as pre
import sqlalchemy

import sys
sys.path.append('C:/Users/Diego Fernandez/Documents/GitHub/Api-Python/Api-Ptyhon/Sistemas_Reglas/principal_SR')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Mysql Connection¿
app.config['MYSQL_HOST'] = 'finalproject.csl9lso2teho.us-east-1.rds.amazonaws.com' 
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'dbFinalProject'
mysql = MySQL(app)


# Funcion con la consultará el usuario por el id de este mismo
@app.route('/getUsuario/<id>', methods=['GET'])
def getUsuario(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Usuario WHERE Id = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id': result[0], 'Nombre': result[1], 'Apellidos' : result[2], 'Contrasena' : result[3]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

################################################################## PREDICCIONES #################################################################### 
# Funcion con la entrenará el algoritmo de prediccion
@app.route('/getAllTrainPredict/<totalBateria>/<bluetooth>/<procesador>/<dualSim>/<mgPixelesFront>/<tecnology4G>/<internalMemory>/<m_depp>/<peso_Telefono>/<number_cores>/<mgPixelesPrimeary>/<px_height>/<px_widht>/<ram_memory>/<sc_h>/<sc_w>/<time_charger>/<tecnologia_3g>/<pantalla_tactil>/<wifi>', methods=['GET'])
def getAllTrainPredict(totalBateria, bluetooth, procesador, dualSim, mgPixelesFront, tecnology4G, internalMemory, m_depp, peso_Telefono, number_cores, mgPixelesPrimeary, px_height, px_widht, ram_memory, sc_h, sc_w, time_charger, tecnologia_3g, pantalla_tactil, wifi):
    return(pre.prediccion(totalBateria, bluetooth, procesador, dualSim, mgPixelesFront, tecnology4G, internalMemory, m_depp, peso_Telefono, number_cores, mgPixelesPrimeary, px_height, px_widht, ram_memory, sc_h, sc_w, time_charger, tecnologia_3g, pantalla_tactil, wifi))

# Funcion que va a insertar datos en la tabla de prediccion
@app.route('/add_Predict', methods=['POST'])
def add_predict():
    try:
        if request.method == 'POST':
            Fecha = request.json['Fecha']
            Usuario_Id = request.json['Usuario_Id']
            totalBateria = request.json['totalBateria']
            bluetooth = request.json['bluetooth']
            procesador = request.json['procesador']
            dualSim = request.json['dualSim']
            mgPixelesFront = request.json['mgPixelesFront']
            tecnology4G = request.json['tecnology4G']
            internalMemory = request.json['internalMemory']
            m_depp = request.json['m_depp']
            peso_Telefono = request.json['peso_Telefono']
            number_cores = request.json['number_cores']
            mgPixelesPrimeary = request.json['mgPixelesPrimeary']
            px_height = request.json['px_height']
            px_widht = request.json['px_widht']
            ram_memory = request.json['ram_memory']
            sc_h = request.json['sc_h']
            sc_w = request.json['sc_w']
            time_charger = request.json['time_charger']
            tecnologia_3g = request.json['tecnologia_3g']
            pantalla_tactil = request.json['pantalla_tactil']
            wifi = request.json['wifi']
            Precio = request.json['Precio']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Prediccion (Fecha, Usuario_Id, totalBateria, bluetooth, procesador, dualSim, mgPixelesFront, tecnology4G, internalMemory, m_depp, peso_Telefono, number_cores, mgPixelesPrimeary, px_height, px_widht, ram_memory, sc_h, sc_w, time_charger, tecnologia_3g, pantalla_tactil, wifi, Precio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (Fecha ,Usuario_Id ,totalBateria ,bluetooth ,procesador ,dualSim ,mgPixelesFront ,tecnology4G ,internalMemory ,m_depp ,peso_Telefono ,number_cores ,mgPixelesPrimeary ,px_height ,px_widht ,ram_memory ,sc_h ,sc_w ,time_charger ,tecnologia_3g ,pantalla_tactil ,wifi ,Precio))
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso"})
        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

############################################################### SISTEMA DE REGLAS ################################################################### 
# Funcion con la consultará el usuario por el id de este mismo
@app.route('/getSistemaReglas/<v_repiratorio>/<v_fatiga>/<v_dolor>/<v_cuello>/<v_debiliad>', methods=['GET'])
def getSistemaReglas(v_repiratorio, v_fatiga, v_dolor, v_cuello, v_debiliad):
    sys.preguntas(v_repiratorio, v_fatiga, v_dolor, v_cuello, v_debiliad)
    return "1"


# Funcion que va a insertar datos en la tabla de prediccion
@app.route('/add_Sistemareglas', methods=['POST'])
def add_Sistemareglas():
    try:
        if request.method == 'POST':
            V_Respiratorio = request.json['V_Respiratorio']
            V_Fatiga = request.json['V_Fatiga']
            V_DolorArticular = request.json['V_DolorArticular']
            V_CuelloHinchado = request.json['V_CuelloHinchado']
            V_Debilidad = request.json['V_Debilidad']
            Respuesta = request.json['Respuesta']
            Fecha = request.json['Fecha']
            Id_Usuario = request.json['Id_Usuario']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Sistema_Reglas (V_Respiratorio, V_Fatiga, V_DolorArticular, V_CuelloHinchado, V_Debilidad, Respuesta, Fecha, Id_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (V_Respiratorio, V_Fatiga, V_DolorArticular, V_CuelloHinchado, V_Debilidad, Respuesta, Fecha, Id_Usuario))
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso"})
        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})



# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)