def convertir_en_romano(numero):
    """
    Restricciones:
        - Es un número natural
        - El número está entre 0 y 3999
            - no es negativo
            - no es mayor que 3999
    Resultado es una cadena que contiene (I, V, X, L, C, D, M)
    Ideas para comprobar un entero:
            - (X) isdigit(): porque no aplica a cualquier cosa que no sea cadena
        - (V) convertir a int y si no se puede, error
        - (V) isinstance()
            - (V) type()
            - (X) isnumeric()
    Pasos:
        1. Validar la entrada
        2a. Si es válido: lo convierto
        2b. Si no es válido: muestro un error
    """

    if not isinstance(numero, int):
        return "No has introducido un número"
    if numero < 1 or numero > 3999:
        return "El número introducido no es válido (debe ser positivo y menor que 4000)"

    # continuamos con la conversión

print(convertir_en_romano("3a3"))
print(convertir_en_romano(-3))
print(convertir_en_romano(3333))
# convertir_en_romano("a")