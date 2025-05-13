# Encuesta sobre transporte estudiantil en la UAM
#Implemente un programa que simule una encuesta realizada en la UAM para conocer los medios
#de transporte utilizados por los estudiantes. Considere tres facultades, cada una con dos
#carreras, y en cada carrera se entrevistarán a cinco estudiantes. Por cada estudiante se debe
#registrar si utiliza bus, motocicleta, taxi, bicicleta o camina. Al final, se mostrarán los totales por
#medio de transporte, desglosados por facultad y el total general. Utilice estructuras cíclicas
#anidadas.



facultades = {
    "Facultad de Ingeniería": ["Ingeniería Civil", "Ingeniería Mecánica"],
    "Facultad de Ciencias": ["Matemáticas", "Física"],
    "Facultad de Humanidades": ["Historia", "Filosofía"]
}


opciones_transporte = ["bus", "motocicleta", "taxi", "bicicleta", "camina"]


resultados = {facultad: {transporte: 0 for transporte in opciones_transporte} for facultad in facultades}


total_general = {transporte: 0 for transporte in opciones_transporte}


for facultad, carreras in facultades.items():
    print(f"\nFacultad: {facultad}")
    for carrera in carreras:
        print(f"  Carrera: {carrera}")
        for estudiante in range(1, 6):  
            print(f"    Estudiante {estudiante}:")
            print("      Opciones de transporte: bus, motocicleta, taxi, bicicleta, camina")
            while True:
                transporte = input("      Ingrese el medio de transporte utilizado: ").lower()
                if transporte in opciones_transporte:
                    resultados[facultad][transporte] += 1
                    total_general[transporte] += 1
                    break
                else:
                    print("      Opción inválida. Intente nuevamente.")


print("\nResultados por facultad:")
for facultad, transportes in resultados.items():
    print(f"\nFacultad: {facultad}")
    for transporte, total in transportes.items():
        print(f"  {transporte.capitalize()}: {total}")

print("\nTotal general:")
for transporte, total in total_general.items():
    print(f"  {transporte.capitalize()}: {total}")