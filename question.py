import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    """
    Args:
    dificultad (str): Nivel de dificultad.

    Returns:
    tuple: Enunciado y alternativas mezcladas.
    """
    pool = p.pool_preguntas[dificultad]
    preguntas_disponibles = list(pool.keys())
    
    if not preguntas_disponibles:
        raise ValueError("No hay más preguntas disponibles.")
    
    n_elegido = random.choice(preguntas_disponibles)
    pregunta = pool.get(n_elegido)
    if pregunta is None:
        raise ValueError(f"La pregunta '{n_elegido}' no está disponible.")
    
    del pool[n_elegido]
    
    alternativas = shuffle_alt(pregunta)
    
    return pregunta['enunciado'], alternativas


if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')