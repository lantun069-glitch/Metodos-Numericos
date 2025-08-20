# Funciones auxiliares para trabajar con matrices y vectores (sin usar NumPy).
from typing import List

Numero = float

def es_casi_cero(x: Numero, tol: float = 1e-12) -> bool:
    """True si |x| < tol."""
    return abs(x) < tol

def clonar_matriz(A: List[List[Numero]]) -> List[List[Numero]]:
    """Copia de la matriz A."""
    return [fila[:] for fila in A]

def intercambiar_filas(A: List[List[Numero]], b: List[Numero], i: int, j: int) -> None:
    """Intercambia fila i con fila j, en A y b (in place)."""
    if i == j:
        return
    A[i], A[j] = A[j], A[i]
    b[i], b[j] = b[j], b[i]

def producto_diagonal(A: List[List[Numero]]) -> Numero:
    """Producto de la diagonal principal de A."""
    n = len(A)
    prod = 1.0
    for i in range(n):
        prod *= A[i][i]
    return prod

def mostrar_matriz(A: List[List[Numero]], ancho: int = 10, prec: int = 6) -> str:
    """String con la matriz A formateada."""
    fmt = f"{{:{ancho}.{prec}f}}"
    lineas = []
    for fila in A:
        lineas.append("[" + " ".join(fmt.format(x) for x in fila) + "]")
    return "\n".join(lineas)

def mostrar_vector(v: List[Numero], ancho: int = 10, prec: int = 6) -> str:
    """String con el vector v formateado."""
    fmt = f"{{:{ancho}.{prec}f}}"
    return "[" + ", ".join(fmt.format(x) for x in v) + "]"
