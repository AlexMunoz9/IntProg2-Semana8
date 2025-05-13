
carreras = {
    "Sistemas": ["Año 1", "Año 2", "Año 3"],
    "Marketing": ["Año 1", "Año 2", "Año 3"],
    "Derecho": ["Año 1", "Año 2", "Año 3"]
}


resultados = {carrera: 0 for carrera in carreras}


total_general = 0


for carrera, años in carreras.items():
    print(f"\nCarrera: {carrera}")
    for año in años:
        print(f"  {año}:")
        for seccion in range(1, 3):  # Dos secciones por año
            while True:
                try:
                    participantes = int(input(f"    Sección {seccion} - Ingrese el número de participantes: "))
                    if participantes >= 0:
                        resultados[carrera] += participantes
                        total_general += participantes
                        break
                    else:
                        print("    El número de participantes no puede ser negativo. Intente nuevamente.")
                except ValueError:
                    print("    Entrada inválida. Por favor, ingrese un número entero.")

# Mostrar resultados
print("\nResultados por carrera:")
for carrera, total in resultados.items():
    print(f"  {carrera}: {total} participantes")

print(f"\nTotal general de participantes: {total_general}")