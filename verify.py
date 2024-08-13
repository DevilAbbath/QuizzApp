import preguntas as p

def verificar(alternativas, eleccion):
    """
    Args:
    alternativas (list): Alternativas de la pregunta.
    eleccion (str): Elección del usuario ('a', 'b', 'c', 'd').

    Returns:
    bool: True si la elección es correcta, False en caso Erroneo.
    """
    indices = ['a', 'b', 'c','d']
    try:
        index = indices.index(eleccion)
    except ValueError:
        print ("Error en su eleccion")
        return False
    
    correcta = alternativas[index][1] == 1

    if correcta:
        print ("Has Acertado!!")
    else:
        print ("Mejor Suerte para la proxima")

    return correcta



if __name__ == '__main__':
    from print_preguntas import print_pregunta

    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)