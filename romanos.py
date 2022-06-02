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
    millares = [ "", "M", "MM", "MMM" ]
    centenas = [ "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ]
    decenas = [ "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
    unidades = [ "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ]

    conversores = [millares, centenas, decenas, unidades]

    if not isinstance(numero, int):
        return "No has introducido un número"
    if numero < 1 or numero > 3999:
        return "El número introducido no es válido (debe ser positivo y menor que 4000)"

    divisores = [1000, 100, 10, 1]
    factores = []

    for divisor in divisores:
        cociente = numero // divisor
        resto = numero % divisor
        factores.append(cociente)
        numero = resto

    resultado = ""
    for pos, factor in enumerate(factores):
        resultado = resultado + conversores[pos][factor]

    return resultado


def convertir_a_numero(romano):
    """
    MCXXIII: 1123
        - de izquierda a derecha
        - convertir cada letra en su valor
        - sumo los valores si a la izquierda hay un dígito mayor que a la derecha
            - VI: sumo ==> 6
        - resto si el valor de la izquierda es menor que el de la derecha
            - IV: resto ==> 4

        1. leo una letra y guardo su valor (letra1)
        2. leo otra letra (letra2)
            2a. si letra2 > letra1 =>  resultado = letra2 - letra1
            2b. si no => resultado letra2 + letra1
    """

    digitos_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    resultado = 0
    anterior = 0
    for letra in romano:
        actual = digitos_romanos[letra]

        if anterior >= actual:
            resultado = resultado + actual
        else:
            resultado = resultado - anterior
            resultado = resultado + (actual - anterior)

        anterior = actual
    return resultado


print(
    convertir_a_numero("IV")
)
print(
    convertir_a_numero("X")
)
print(
    convertir_a_numero("MCXXIII")
)
print(
    convertir_a_numero("IC")
)