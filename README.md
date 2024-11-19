A continuación se muestra el razonamiento para haber llegado a la solución:
  
-Punto 1: Para poder realizar las operaciones, el usuario debe introducir, en principio, 
  dos números cualesquiera. Por lo tanto, la entrada proporcionada por el usuario debe 
  poder convertirse a float, lo cual se comprueba con la función compruebe().
  
  Luego, se revisan las condiciones de cada operación, siendo la más problemática la
  división, puesto que no se puede dividir entre cero. Siendo así, se crea una condición
  para usar el operador división (/), en la que se arroja un error si el segundo número es cero.
  
  Finalmente, se debe comprobar que el usuario haya elegido uno de los cuatro símbolos 
  diponibles, de modo que quede claro el tipo de operación que desea realizar.

-Punto 2: En este caso el usuario debe insertar una palabra para comprobar si es un palíndromo, lo
  que quiere decir que la palabra insertada debe leerse igual al derecho y al revés. Teniendo en
  cuenta lo anterior, se crea una función que retorne un booleano de acuerdo a la similitud entre
  la palabra dada y su reverso, proceso que es realizando con la indexación.

-Punto 3: Para poder realizar las operaciones, el usuario debe introducir, en principio, 
  dos números naturales cualesquiera, puesto que se buscan números primos. Por lo tanto, la entrada 
  proporcionada por el usuario debe poder convertirse a int y ser mayor a cero, lo cual se comprueba 
  con la función compruebe().

  Finalmente, se identifica el número primo usando la Prueba de Primalidad, donde se prueban los 
  números naturales que estén por debajo de la raíz del número a evaluar para ver si alguno es 
  divisor, a excepción del uno.
  
-Punto 4: En este caso el usuario debe insertar una lista de números para buscar la suma más grande de
  dos números consecutivos, lo que significa que la lista debe tener únicamente números enteros. Teniendo en
  cuenta lo anterior, se crea una función que compruebe que se puede transformar cada valor en la lista a
  int.
  
  Luego, se busca la pareja cuya suma dé el valor máximo posible, tarea realizada con un bucle.

-Punto 5: Para este programa se debe de comprobar primero que la lista no esté vacía ni que contenga un solo
  elemento. Después de haberlo comprobado, se debe crear una "palabra" clave que contenga las letras de cada
  anagrama, para a continuación comparar cada palabra y encontrar las que sí son anagramas. Esta operación es
  realizada con la herramienta diccionario.
