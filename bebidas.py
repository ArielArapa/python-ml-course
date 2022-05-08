bebidas = {
    "Alcohol" : [
        {"nombre": "Cerveza Api", "precio": 123, "porAlcohol": 4.5},
        {"nombre": "Cerveza Ipa", "precio": 150, "porAlcohol": 11.5},
        {"nombre": "Wisky", "precio": 131, "porAlcohol": 2.5},
        {"nombre": "Ron", "precio": 176, "porAlcohol": 6.5},
        {"nombre": "Moster Inc.", "precio": 132, "porAlcohol": 10.5},
        {"nombre": "Adolf", "precio": 200, "porAlcohol": 14.5},
        {"nombre": "Lord Ma", "precio": 143, "porAlcohol": 9.5}
    ],
    "SinAlcohol" : [
        {"nombre" : "Jugo Naranja", "precio" : 100},
        {"nombre" : "Jugo Limon", "precio" : 89},
        {"nombre" : "Jugo Banana", "precio" : 43},
        {"nombre" : "Jugo Frutilla", "precio" : 76},
        {"nombre" : "Jugo Manazana", "precio" : 59},
        {"nombre" : "Agua", "precio" : 90}
    ]
}

#Supongamos que es una base de datos.
#Adaptación al sistema ya hecho.

#Tareas a realizar:
#_ Preguntar por consola si desea un menú segun porcentaje de alcohol
#   | Ejemplo: Si desea tomar solo bebidas que tenga más de 10% de alcohol mostrar solo esas bebidas y precio

#_ Preguntar por consola si desea un menú segun el precio
#   | Si desea tomar solo bebidas que tengan un precio inferior o superior a 100$ mostrar esas bebidas y precio

#_ O si desea ver el menú completo, solamente.

numeros = [2, 5, 10, 23, 50, 33]

lista = []
def alguito (numero, por, signo):
    if numero < por and signo == "menor":
        lista.append(numero)
    elif numero > por and signo == "mayor":
        lista.append(numero)


for num in numeros:
    alguito(num, 11, "mayor")

print(lista)