import math

Numeros = []

while True:
    Numeros = input(input("Introduce los numeros que quieras para el Calculo"))

    if Numeros == "":
        break

Media = sum(Numeros) / len(Numeros)
Varianza = Media / len(Numeros)

Desviacion_Estandar = math.sqrt(Varianza)

print(Media)
print(Varianza)
print(Desviacion_Estandar)