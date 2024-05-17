import os

def calcular_costo_envio(nombre_cliente, peso_paquete, distancia_envio):
    try:
        peso_paquete = float(peso_paquete)
        distancia_envio = float(distancia_envio)
        if peso_paquete <= 0 or distancia_envio <= 0:
            raise ValueError("El peso y la distancia deben ser valores numéricos positivos.")
    except ValueError as e:
        return str(e)

    costo_base = 5000  # CLP
    adicional_peso = 500 * peso_paquete  # CLP por kilogramo
    recargo_distancia = 0
    
    if distancia_envio > 100:
        recargo_distancia = 100 * (distancia_envio - 100)  # CLP por kilómetro extra

    costo_total = costo_base + adicional_peso + recargo_distancia
    return costo_base, adicional_peso, recargo_distancia, costo_total

def mostrar_desglose(nombre_cliente, peso_paquete, distancia_envio, costo_base, adicional_peso, recargo_distancia, costo_total):
    print("\n--- Desglose del Costo de Envío ---")
    print(f"Cliente: {nombre_cliente}")
    print(f"Peso del paquete: {peso_paquete} kg")
    print(f"Distancia de envío: {distancia_envio} km")
    print(f"Costo base: ${costo_base} CLP")
    print(f"Adicional por peso: ${adicional_peso} CLP")
    if recargo_distancia > 0:
        print(f"Recargo por distancia: ${recargo_distancia} CLP")
    print(f"Costo total de envío: ${costo_total} CLP")

def generar_archivo_envio(nombre_cliente, peso_paquete, distancia_envio, costo_total):
    nombre_archivo = f"envio_{nombre_cliente.replace(' ', '_')}.txt"
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("--- Detalles del Envío ---\n")
        archivo.write(f"Cliente: {nombre_cliente}\n")
        archivo.write(f"Peso del paquete: {peso_paquete} kg\n")
        archivo.write(f"Distancia de envío: {distancia_envio} km\n")
        archivo.write(f"Costo total de envío: ${costo_total} CLP\n")

def main():
    while True:
        nombre_cliente = input("Ingrese el nombre del cliente (máximo 30 caracteres): ").strip()
        if len(nombre_cliente) == 0 or len(nombre_cliente) > 30:
            print("El nombre del cliente no puede estar vacío y debe tener máximo 30 caracteres.")
            continue

        peso_paquete = input("Ingrese el peso del paquete en kilogramos: ")
        distancia_envio = input("Ingrese la distancia de envío en kilómetros: ")

        resultado = calcular_costo_envio(nombre_cliente, peso_paquete, distancia_envio)
        if isinstance(resultado, str):
            print("Error:", resultado)
            continue

        costo_base, adicional_peso, recargo_distancia, costo_total = resultado

        mostrar_desglose(nombre_cliente, peso_paquete, distancia_envio, costo_base, adicional_peso, recargo_distancia, costo_total)

        generar_archivo_envio(nombre_cliente, peso_paquete, distancia_envio, costo_total)

        opcion = input("\n¿Desea calcular el costo de envío para otro paquete? (s/n): ")
        if opcion.lower() != 's':
            break

if __name__ == "__main__":
    main()
