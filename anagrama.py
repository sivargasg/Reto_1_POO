def compruebe(entrada):
    """ 
    Comprueba si la entrada contiene más de una palabra. 
    
    Parámetros: entrada (str): Cadena de texto con palabras separadas 
    por comas. 
    
    Retorna: bool: True si la lista contiene más de una palabra, 
    False en caso contrario. 
    """
    lista = entrada.split(",")
    lista = [elemento.strip() for elemento in lista]        
    if len(lista) <= 1:
        return False
    return True

def anagramas(entrada):
    """ 
    Encuentra todos los anagramas en una lista de palabras. 
    
    Parámetros: entrada (str): Cadena de texto con palabras separadas 
    por comas. 
    
    Retorna: list: Lista de palabras que son anagramas entre sí. 
    """
    lista = entrada.split(",")
    lista = [elemento.strip() for elemento in lista]
    lista_anagramas = []
    diccionario_anagramas = {}
    for palabra in lista:
        palabra_ordenada = ''.join(sorted(palabra))
        if palabra_ordenada in diccionario_anagramas: #palabra_ordenada se vuelve una clave dentro del diccionario
            diccionario_anagramas[palabra_ordenada].append(palabra) #Se añade la palabra como otro valor de una clave ya usada
        else:
            diccionario_anagramas[palabra_ordenada] = [palabra] #Se pone la palabra dada como el único valor para la clave
    for grupo in diccionario_anagramas.values():
        if len(grupo) > 1:
            lista_anagramas.extend(grupo)
    return lista_anagramas

if __name__ == "__main__":
    entrada = input("Ingrese su lista de palabras, separadas por comas: ")
    if compruebe(entrada):
        print(f"Los anagramas en su lista son: {anagramas(entrada)}")
    else:  
        print(f"Efectivamente, ({entrada}) es anagrama de sí mismo")
