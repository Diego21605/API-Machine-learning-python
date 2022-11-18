from random import choice
import Sistemas_Reglas.sistemadereglas

## creacion del objeto
engine = Sistemas_Reglas.sistemadereglas()
### reset Preparar el motor para la ejecución.
engine.reset()

class principal_SR:
    def preguntas(v_repiratorio, v_fatiga, v_dolor, v_cuello, v_debiliad):
        
        engine.declare(Sistemas_Reglas.sistemadereglas.reglas(respiratorio=choice([str(v_repiratorio)])))        
        engine.declare(Sistemas_Reglas.sistemadereglas.reglas(fatiga=choice([str(v_fatiga)])))        
        engine.declare(Sistemas_Reglas.sistemadereglas.reglas(dolor=choice([str(v_dolor)])))        
        engine.declare(Sistemas_Reglas.sistemadereglas.reglas(cuello=choice([str(v_cuello)])))        
        engine.declare(Sistemas_Reglas.sistemadereglas.reglas(debilidad=choice([str(v_debiliad)])))
        
        engine.run()