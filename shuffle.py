import preguntas as p
import random

def shuffle_alt(pregunta):
    """
    Args:
    pregunta (data): Pregunta con alternativas.

    Returns:
    list: Alternativas mezcladas.
    """
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    return alternativas

if __name__ == '__main__':
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print(shuffle_alt(pregunta))