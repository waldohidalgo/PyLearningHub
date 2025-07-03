import random

def lanzar_dados(n=1):
    if n < 1:
        raise ValueError("Debes lanzar al menos un dado")
    return [random.randint(1, 6) for _ in range(n)]