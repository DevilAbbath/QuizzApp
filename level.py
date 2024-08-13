def choose_level(n_pregunta, p_level):
    """
    Args:
    n_pregunta (int): Number Quest.
    p_level (int): Quest for Level.

    Returns:
    str: dificultad ('basicas', 'intermedias', 'avanzadas').
    """

    if p_level == 1:
        if n_pregunta == 1:
            level = 'basicas'
        elif n_pregunta == 2:
            level = 'intermedias'
        elif n_pregunta == 3:
            level = 'avanzadas'
        else:
            raise ValueError(f"Pregunta número {n_pregunta} fuera del rango para p_level = {p_level}.")
    
    elif p_level == 2:
        if 1 <= n_pregunta <= 2:
            level = 'basicas'
        elif 3 <= n_pregunta <= 4:
            level = 'intermedias'
        elif 5 <= n_pregunta <= 6:
            level = 'avanzadas'
        else:
            raise ValueError(f"Pregunta número {n_pregunta} fuera del rango para p_level = {p_level}.")
    
    elif p_level == 3:
        if 1 <= n_pregunta <= 3:
            level = 'basicas'
        elif 4 <= n_pregunta <= 6:
            level = 'intermedias'
        elif 7 <= n_pregunta <= 9:
            level = 'avanzadas'
        else:
            raise ValueError(f"Pregunta número {n_pregunta} fuera del rango para p_level = {p_level}.")
    
    else:
        raise ValueError(f"Valor no válido para selector de nivel: {p_level}. Debe ser 1, 2 o 3.")
    
    return level

if __name__ == '__main__':
    # Verificar resultados
    print(choose_level(1, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(5, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias
    print(choose_level(8, 3))  # avanzadas