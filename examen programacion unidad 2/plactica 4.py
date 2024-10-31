#4
#Escribir un programa que almacene las
#asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
#Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada
#asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es
#cada una des las asignaturas de la lista y <nota> cada una de las
#correspondientes notas introducidas por el usuario.
# Lista de asignaturas
print("")#implime espacio blanco
print("Castruita Soto Emmanuel 3W 1176")#implime datos del alumno
print("")#implime espacio blanco
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]# se conocen las materias
notas = {}# Diccionario para almacenar las notas
# Preguntar al usuario la nota de cada asignatura
for asignatura in asignaturas:
    try:
        nota = float(input(f"¿Qué nota sacaste en {asignatura}? "))#se pediran datos y al ingresarlos se pasaran a una nueva lista 
        notas[asignatura] = nota
    except ValueError:#sino se pone ningun numero mostrara un mensaje
        print("Por favor, introduce un número válido.")#este mensaje 
for asignatura, nota in notas.items():# Mostrar las notas
    print(f"En {asignatura} has sacado {nota}")#se muestra la asignatura con su calificacion

