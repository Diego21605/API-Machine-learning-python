import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
import sqlalchemy

def prediccion(totalBateria, bluetooth, procesador, dualSim, mgPixelesFront, tecnology4G, internalMemory, m_depp, peso_Telefono, number_cores, mgPixelesPrimeary, px_height, px_widht, ram_memory, sc_h, sc_w, time_charger, tecnologia_3g, pantalla_tactil, wifi):
    # Cargamos el dataset
    conn = sqlalchemy.create_engine("mysql+pymysql://admin:admin123@finalproject.csl9lso2teho.us-east-1.rds.amazonaws.com:3306/dbFinalProject")
    df = pd.read_sql_table("TrainPredict", conn)
    # Descripción genereal del conjunto de datos
    df.describe()

    df.head()

    df.columns

    df.loc[(df['price_range'] ==0), 'price_range'] = 'Low Cost'
    df.loc[(df['price_range'] ==1), 'price_range'] = 'Medium Cost'
    df.loc[(df['price_range'] ==2), 'price_range'] = 'High Cost'
    df.loc[(df['price_range'] ==3), 'price_range'] = 'Very High Cost'

    df.head()

    df.info()

    # Dividimos los datos en entrenamiento y prueba
    from sklearn.model_selection import train_test_split
    # X son nuestras variables independientes
    X = df.drop(["price_range"],axis = 1)

    # y es nuestra variable dependiente
    y = df.price_range

    # División 75% de datos para entrenamiento, 25% de daatos para test
    X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=0)

    # Creaamos el modelo de Bosques Aleatorios (y configuramos el número de estimadores (árboles de decisión))
    BA_model = RandomForestClassifier(n_estimators = 19, 
                                    random_state = 2016,
                                    min_samples_leaf = 8,)

    BA_model.fit(X_train, y_train)

    BA_model.score(X_test, y_test)


    # Predicción del modelo usando los datos de prueba
    y_pred = BA_model.predict(X_test)
    matriz = confusion_matrix(y_test,y_pred)

    plot_confusion_matrix(conf_mat=matriz, figsize=(6,6), show_normed=False)
    plt.tight_layout()

    arr = [totalBateria, bluetooth, procesador, dualSim, mgPixelesFront, tecnology4G, internalMemory, m_depp, peso_Telefono, number_cores, mgPixelesPrimeary, px_height, px_widht, ram_memory, sc_h, sc_w, time_charger, tecnologia_3g, pantalla_tactil, wifi]

    Z_pred = BA_model.predict([arr])

    predict = str(Z_pred)
    characters = "[']"

    for character in characters:
        predict = predict.replace(character, "")

    print("Predict: " + predict)
    return ("El costó será : " + predict)