def palindromo(palabra):
    """
    Verifica si una palabra es un palíndromo.

    Parámetros:
    palabra (str): La palabra a verificar.

    Retorna:
    bool: True si la palabra es un palíndromo, False en caso contrario.
    """
    palabra = palabra.lower() #escribe toda la palabra en minúscula para evitar errores
    largo = len(palabra)
    for n in range(largo // 2):
        if palabra[n] != palabra[largo - 1 - n]:
            return False
    return True
   
if __name__ == "__main__":
    palabra = input("Inserte la palabra a analizar: ")
    if palindromo(palabra):
        print(palabra + " sí es un palíndromo.")
    else:
        print(palabra + " no es un palíndromo.")
