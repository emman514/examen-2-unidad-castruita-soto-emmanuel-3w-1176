#3                                                                                       
#Escribir un programa que pregunte al usuario su nombre, edad, dirección y
#teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
#mensaje <nombre> tiene
#<edad> años, vive en <dirección> y su número de teléfono es
#<teléfono>.
print("")#implime espacio blanco
print("Castruita Soto Emmanuel 3W 1176")#implime datos del alumno
print("")#implime espacio blanco
datos_personales = {}# s3 crea una lista vacia 

# Preguntar al usuario por sus datos
datos_personales['nombre'] = input("¿Cuál es tu nombre? ")# se agregara a la lita el nombre que tu pongas
datos_personales['edad'] = input("¿Cuál es tu edad? ")# se agregara a la lita la edad  tu pongas
datos_personales['dirección'] = input("¿Cuál es tu dirección? ")# se agregara a la lita dirreccion que tu pongas
datos_personales['teléfono'] = input("¿Cuál es tu número de teléfono? ")# se agregara a la lita el telefono que tu pongas
# Mostrar los datos totales que son nombre edad direccion numero d3e cel
print(f"{datos_personales['nombre']} tiene {datos_personales['edad']} años, vive en {datos_personales['dirección']} y su número de teléfono es {datos_personales['teléfono']}.")