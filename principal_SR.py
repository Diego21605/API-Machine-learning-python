from random import choice
import sistemadereglas

## creacion del objeto
engine = sistemadereglas()
### reset Preparar el motor para la ejecución.
engine.reset()

def preguntas(v_repiratorio, v_fatiga, v_dolor, v_cuello, v_debiliad):    
    engine.declare(sistemadereglas.reglas(respiratorio=choice([str(v_repiratorio)])))        
    engine.declare(sistemadereglas.reglas(fatiga=choice([str(v_fatiga)])))        
    engine.declare(sistemadereglas.reglas(dolor=choice([str(v_dolor)])))        
    engine.declare(sistemadereglas.reglas(cuello=choice([str(v_cuello)])))        
    engine.declare(sistemadereglas.reglas(debilidad=choice([str(v_debiliad)])))
    
    engine.run()