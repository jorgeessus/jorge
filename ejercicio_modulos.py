import math

## pi = 3.1416
pi = math.pi

def ara_circunferencia(radio):
    area = pi * radio ** 2 
    return area 

def raiz_cuadrada(numero):
    raiz_cuadrada = math.sqrt(numero)
    return raiz_cuadrada

def ejecutar_codigo():
    print()
    radio = float(input("ingrese el radio de la circunferencia: "))
    print()
    resoyesta_1 = area_circunferencia(radio)
    numero = float(input("ingrese un numero: "))
    print()
    respuesta_2 = raiz_cuardrada(numero)

    print(f"el area de la circunferencia {radio} = {respuesta_2}")
    print()
    print(f"la raiz cuadrada de {numero} = {respuesta_2}")
    print()

numero = float(input("Ingrese el numero: "))
print()
raiz_cuadrada = math.sqrt(numero)
print(f"la raiz cuadrada de {numero} = {raiz_cuadrada}")
print()