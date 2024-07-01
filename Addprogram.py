def obtener_numeros():
    numeros = []
    while True:
        entrada = input("Introduce un número (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido.")
    return numeros

def calcular_suma_min_max(numeros):
    if not numeros:
        return 0, None, None
    suma = sum(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return suma, minimo, maximo

def main():
    numeros = obtener_numeros()
    suma, minimo, maximo = calcular_suma_min_max(numeros)
    print(f"Suma: {suma}")
    if minimo is not None and maximo is not None:
        print(f"Mínimo: {minimo}")
        print(f"Máximo: {maximo}")

if __name__ == "__main__":
    main()
