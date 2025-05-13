#Control de venta de vigorón en feria universitaria UAM

print("Bienvenido al sistema de venta de vigorón en la feria UAM")
clientes_atendidos = int(input("Ingrese la cantidad de clientes atendidos: "))
total_ventas = 0
for cliente in range( clientes_atendidos):
    print(f"\nCliente {cliente + 1}")
    
    porciones = int(input("Ingrese la cantidad de porciones de vigorón: "))
    
    total_cliente = 0
    
    for porcion in range(porciones):
        precio_unitario = float(input(f"Ingrese el precio de la porción {porcion}: "))
        total_cliente += precio_unitario
        
    print(f"El total a pagar por el cliente {cliente } es: {total_cliente:.2f}")
    total_ventas += total_cliente
print(f"\nEl total de ventas del día es: {total_ventas:.2f}")
       


    