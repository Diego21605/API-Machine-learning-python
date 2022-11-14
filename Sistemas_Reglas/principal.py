from random import choice
from sistemaReglas import *

## creacion del objeto
engine = sistemadereglas()
### reset Preparar el motor para la ejecución.
engine.reset()

def preguntas(v_repiratorio, v_fatiga, v_dolor, v_cuello, v_debiliad):
    
    engine.declare(reglas(respiratorio=choice([str(v_repiratorio)])))
    
    engine.declare(reglas(fatiga=choice([str(v_fatiga)])))
    
    engine.declare(reglas(dolor=choice([str(v_dolor)])))
    
    engine.declare(reglas(cuello=choice([str(v_cuello)])))
    
    engine.declare(reglas(debilidad=choice([str(v_debiliad)])))