from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, World!'

app.run()


""" 

1. Problemas respiratorios #Diabetes
2. Fatiga #Diabetes - Hipertiroidismo - Hipotiroidismo
3. Dolor articular #Hipotiroidismo
4. Cuello hinchado #Hipotiroidismo - Hipertiroidismo
5. Debilidad muscular #Hipertiroidismo


"""