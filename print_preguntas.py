import preguntas as p

def print_pregunta(enunciado, alternativas):
    """
    Args:
    enunciado (list): Enunciado de la pregunta.
    alternativas (list): Alternativas de la pregunta.
    """
    print ('\n'.join(enunciado))
    letras = ['A', 'B', 'C', 'D']
    
    for letra, alternativa in zip(letras, alternativas):
        print (f'{letra}. {alternativa[0]}')
    

if __name__ == '__main__':
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])