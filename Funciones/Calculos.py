import math

def areaRectangulo(*, base: float = 9, altura: float = 10):
    return base * altura

def areaCirculo(radio: float = 2):
    return math.pi * radio**2

def areaTriangulo(base: float = 1, altura: float = 10):
    return base * altura / 2