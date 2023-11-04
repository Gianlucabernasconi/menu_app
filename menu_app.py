compras_usuario = []

def agregar_compra():
    compra = input("Ingrese el monto de la compra: ")
    try:
        compra = float(compra)
        if compra > 0:
            compras_usuario.append(compra)
            print("Su compra se agregó correctamente.")
        else:
            print("El monto de la compra debe ser mayor que cero.")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

def mostrar_compras():
    numero_compra = 0
    for element in compras_usuario:
        numero_compra += 1
        print(f"Compra {numero_compra}: {element}")
    
    if numero_compra == 0:
        print("No hay compras registradas")

def mostrar_total():
    total = sum(elemento for elemento in compras_usuario if isinstance(elemento, (int, float)))
    print("Monto total de compras:", total)

def main():
    while True:
        print("1. Agregar compra\n2. Mostrar compras\n3. Mostrar total gastado\n4. Salir")
        respuesta = input("Seleccione una opción: ")
        if respuesta == '1':
            agregar_compra()
        elif respuesta == '2':
            mostrar_compras()
        elif respuesta == '3':
            mostrar_total()
        elif respuesta == '4':
            print("Hasta luego!")
            break


if __name__ == "__main__":
    main()


 