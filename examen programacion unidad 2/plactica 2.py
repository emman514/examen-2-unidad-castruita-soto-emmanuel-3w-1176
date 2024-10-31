#2
#Escribir un programa que almacene el diccionario
#con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y
#después muestre por pantalla los créditos de cada asignatura en el
#formato <asignatura>
#tiene <créditos> créditos, donde <asignatura> es
#cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe
#mostrar también el número total de créditos del curso.
print("")#implime espacio blancso
print("Castruita Soto Emmanuel 3W 1176")#implime datos del alumno
print("")#implime espacio blanco
creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}# se dan a conocer las materias con sus creditos
for asignatura, credito in creditos.items():# Mostrar los créditos de cada asignatura
    print(f"{asignatura} tiene {credito} créditos")#se nimplimira la materia con sus creditos 
# Calcular y mostrar el total de créditos
total_creditos = sum(creditos.values())#se ara una suma para conoserel total
print(f"El número total de créditos del curso es: {total_creditos}")# se3 implime el total de creditos
