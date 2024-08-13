def validate(opciones, eleccion):
    """
    Args:
    opciones (list): Lista de opciones.
    eleccion (str): Alternativa que escoge el usuario.

    Returns:
    str: Opción valida.
    """
    while eleccion not in opciones:
        print (f'Opcion Invalida, favor selecione una de las siguientes opciones \n {", ".join(opciones)}')
        eleccion = input('Ingresa una opcion: ').lower()
    return eleccion

if __name__ == '__main__':
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    resultado = validate(numeros, eleccion)
    print (f'Opcion seleccionada: {resultado}')