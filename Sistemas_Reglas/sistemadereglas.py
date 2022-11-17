from Sistemas_Reglas.reglas import *


class sistemadereglas(KnowledgeEngine):


  """ Preguntas
    1. Problemas respiratorios #Diabetes
    2. Fatiga #Diabetes - Hipertiroidismo - Hipotiroidismo
    3. Dolor articular #Hipotiroidismo
    4. Cuello hinchado #Hipotiroidismo - Hipertiroidismo
    5. Debilidad muscular #Hipertiroidismo

    """

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=0)), (reglas(dolor=0)), (reglas(cuello=0)), (reglas(debilidad=0)))
  def m1(self):
    print('Actualmente se no se encuentran anomalias, usted esta sano.')
    return 'Actualmente se no se encuentran anomalias, usted esta sano.'

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=0)), (reglas(dolor=0)), (reglas(cuello=0)), (reglas(debilidad=1)))
  def m2(self):
    print('Posiblemente tengas Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=0)), (reglas(dolor=0)), (reglas(cuello=1)), (reglas(debilidad=0)))
  def m3(self):
    print('Es posible que tengas Hipertiroidismo o Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=0)), (reglas(dolor=0)), (reglas(cuello=1)), (reglas(debilidad=1)))
  def m4(self):
    print('Posiblemente tengas Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=0)), (reglas(dolor=1)), (reglas(cuello=0)), (reglas(debilidad=0)))
  def m5(self):
    print('Posiblemente tengas Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=0)), (reglas(dolor=1)), (reglas(cuello=0)), (reglas(debilidad=1)))
  def m6(self):
    print('Es posible que tengas Hipertiroidismo o Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=0)), (reglas(dolor=1)), (reglas(cuello=1)), (reglas(debilidad=0)))
  def m7(self):
    print('Es posible que tengas Hipertiroidismo o Hipotiroidismo')
  
  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=0)), (reglas(dolor=1)), (reglas(cuello=1)), (reglas(debilidad=1)))
  def m8(self):
    print('Es posible que tengas Hipertiroidismo o Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=1)), (reglas(dolor=0)), (reglas(cuello=0)), (reglas(debilidad=0)))
  def m9(self):
    print('Puede tener diabetes')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=1)), (reglas(dolor=0)), (reglas(cuello=0)), (reglas(debilidad=1)))
  def m10(self):
    print('Alta probabilidad de Hipertiroidismo y una baja de diabetes')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=1)), (reglas(dolor=0)), (reglas(cuello=1)), (reglas(debilidad=0)))
  def m11(self):
    print('Es posible que tengas Hipertiroidismo o Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=1)), (reglas(dolor=0)), (reglas(cuello=1)), (reglas(debilidad=1)))
  def m12(self):
    print('Tienes Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=1)), (reglas(dolor=1)), (reglas(cuello=0)), (reglas(debilidad=0)))
  def m13(self):
    print('Alta probabilidad de tener Hipotiroidismo y una baja probabilidad de diabetes')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=1)), (reglas(dolor=1)), (reglas(cuello=0)), (reglas(debilidad=1)))
  def m14(self):
    print('Alta probabilidad de tener Hipotiroidismo y una baja probabilidad de Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=1)), (reglas(dolor=1)), (reglas(cuello=1)), (reglas(debilidad=0)))
  def m15(self):
    print('Tienes Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=0)), (reglas(fatiga=1)), (reglas(dolor=1)), (reglas(cuello=1)), (reglas(debilidad=1)))
  def m16(self):
    print('Por favor ir a donde un especialista, altas probabilidades de tener Hipotiroidismo o Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=0)), (reglas(dolor=0)), (reglas(cuello=0)), (reglas(debilidad=0)))
  def m17(self):
    print('Es posible que tengas diabetes')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=0)), (reglas(dolor=0)), (reglas(cuello=0)), (reglas(debilidad=0)))
  def m17(self):
    print('Es posible que tengas diabetes')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=0)), (reglas(dolor=0)), (reglas(cuello=0)), (reglas(debilidad=1)))
  def m18(self):
    print('Es posible que tengas diabetes o Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=0)), (reglas(dolor=0)), (reglas(cuello=1)), (reglas(debilidad=0)))
  def m19(self):
    print('Es posible que tengas diabetes o Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=0)), (reglas(dolor=0)), (reglas(cuello=1)), (reglas(debilidad=1)))
  def m20(self):
    print('Es posible que tengas diabetes o Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=0)), (reglas(dolor=1)), (reglas(cuello=0)), (reglas(debilidad=0)))
  def m21(self):
    print('Es posible que tengas diabetes o Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=0)), (reglas(dolor=1)), (reglas(cuello=0)), (reglas(debilidad=1)))
  def m22(self):
    print('Es posible que tengas diabetes o Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=0)), (reglas(dolor=1)), (reglas(cuello=1)), (reglas(debilidad=0)))
  def m23(self):
    print('Tiene una alta probabilidad de tener Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=0)), (reglas(dolor=1)), (reglas(cuello=1)), (reglas(debilidad=1)))
  def m24(self):
    print('Tiene una alta probabilidad de tener Hipotiroidismo o Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=1)), (reglas(dolor=0)), (reglas(cuello=0)), (reglas(debilidad=0)))
  def m25(self):
    print('Es posible que tengas diabetes o Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=1)), (reglas(dolor=0)), (reglas(cuello=0)), (reglas(debilidad=1)))
  def m26(self):
    print('Por favor ir a donde un especialista, altas probabilidades de tener Hipotiroidismo o Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=1)), (reglas(dolor=0)), (reglas(cuello=1)), (reglas(debilidad=0)))
  def m27(self):
    print('Es posible que tengas diabetes o Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=1)), (reglas(dolor=0)), (reglas(cuello=1)), (reglas(debilidad=1)))
  def m28(self):
    print('Por favor ir a donde un especialista, altas probabilidades de tener Hipertiroidismoo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=1)), (reglas(dolor=1)), (reglas(cuello=0)), (reglas(debilidad=0)))
  def m29(self):
    print('Es posible que tengas diabetes o Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=1)), (reglas(dolor=1)), (reglas(cuello=0)), (reglas(debilidad=1)))
  def m30(self):
    print('Tiene una alta probabilidad de tener Hipotiroidismo o Hipertiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=1)), (reglas(dolor=1)), (reglas(cuello=1)), (reglas(debilidad=0)))
  def m31(self):
    print('Por favor ir a donde un especialista, altas probabilidades de tener Hipotiroidismo')

  @Rule(AND(reglas(respiratorio=1)), (reglas(fatiga=1)), (reglas(dolor=1)), (reglas(cuello=1)), (reglas(debilidad=1)))
  def m32(self):
    print('Por favor ir al hospital lo mas pronto posible')

  

""" 

P1	P2	P3	P4	P5
R1	0	0	0	0	0 -
R2	0	0	0	0	1 -
R3	0	0	0	1	0 -
R4	0	0	0	1	1 -
R5	0	0	1	0	0 -
R6	0	0	1	0	1 -
R7	0	0	1	1	0 -
R8	0	0	1	1	1 -
R9	0	1	0	0	0 -
R10	0	1	0	0	1 -
R11	0	1	0	1	0 -
R12	0	1	0	1	1 -
R13	0	1	1	0	0 -
R14	0	1	1	0	1 -
R15	0	1	1	1	0 -
R16	0	1	1	1	1 -
R17	1	0	0	0	0 -
R18	1	0	0	0	1 -
R19	1	0	0	1	0 - 
R20	1	0	0	1	1 - 
R21	1	0	1	0	0 -
R22	1	0	1	0	1 -
R23	1	0	1	1	0 -
R24	1	0	1	1	1 -
R25	1	1	0	0	0 -
R26	1	1	0	0	1 -
R27	1	1	0	1	0 -
R28	1	1	0	1	1 -
R29	1	1	1	0	0 -
R30	1	1	1	0	1 -
R31	1	1	1	1	0 -
R32	1	1	1	1	1 -


"""