def es_par_o_impar(numero):
    """Determina si un número es par o impar."""
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def main():
    print("Determinador de números pares o impares (ingresa 'salir' para finalizar)")
    
    while True:
        # Solicitar al usuario que ingrese un número o que escriba 'salir'
        entrada = input("Ingresa un número entero (o 'salir' para terminar): ")
        
        if entrada.lower() == "salir":
            print("Saliendo del programa...")
            break
        
        try:
            # Convertir la entrada a un número entero
            numero = int(entrada)
            
            # Determinar si el número es par o impar
            resultado = es_par_o_impar(numero)
            
            # Mostrar el resultado
            print(f"El número {numero} es {resultado}.")
        
        except ValueError:
            print("Por favor, ingresa un número válido o 'salir' para finalizar.")

if __name__ == "__main__":
    main()
