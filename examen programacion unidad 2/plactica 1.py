#1
#Escribir un programa que almacene las
#asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
#Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada
#asignatura y elimine de la lista las asignaturas aprobadas. Al final el
#programa debe mostrar por pantalla las asignaturas que el usuario tiene que
#repetir.
print("")#implime espacio blanco
print("Castruita Soto Emmanuel 3W 1176")#implime datos del alumno
print("")#implime espacio blanco
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]#se enseñan las materias en pantalla
asignaturas_repetir = []# Inicializar una lista para las asignaturas que hay que repetir
for asignatura in asignaturas:# Preguntar al usuario la nota de cada asignatura
    try:
        nota = float(input(f"¿Qué nota sacaste en {asignatura}? "))#se le preguntara que nota saco en cada matera
        if nota < 6:  # Supongamos que la nota mínima para aprobar es 6
            asignaturas_repetir.append(asignatura)#si tine menos de 6 la materia se agregara a otrea lista
    except ValueError:#sino pone un numero se implimira un mensaje
        print("Por favor, introduce un número válido.")#este mensaje
if asignaturas_repetir:# Mostrar las asignaturas que hay que repetir
    print("Tienes que repetir las siguientes asignaturas:")#se implimira el mensaje que ay que repetir
    for asignatura in asignaturas_repetir:
        print(f"- {asignatura}")#se implimiran las materias reprobadas
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")# si ninguna materia fue reprobada saldra un mensaje de felizidades
    