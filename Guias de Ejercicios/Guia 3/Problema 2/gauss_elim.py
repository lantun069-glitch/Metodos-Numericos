# Eliminacion Gaussiana con pivoteo parcial (sin NumPy).
from typing import List, Tuple
from utils import es_casi_cero, intercambiar_filas, clonar_matriz, producto_diagonal

Numero = float

class MatrizSingularError(Exception):
    """Excepcion cuando la matriz es singular o casi singular (det ~ 0)."""
    pass

def sustitucion_atras(U: List[List[Numero]], y: List[Numero], tol: float = 1e-12) -> List[Numero]:
    """Resuelve U x = y por sustitucion hacia atras."""
    n = len(U)
    x = [0.0] * n
    
    for i in range(n-1, -1, -1):
        s = y[i]
        for j in range(i+1, n):
            s -= U[i][j] * x[j]
        if es_casi_cero(U[i][i], tol):
            raise MatrizSingularError("Pivote nulo en sustitucion hacia atras.")
        x[i] = s / U[i][i]
    return x

def eliminacion_gaussiana(A: List[List[Numero]], b: List[Numero], *, tol: float = 1e-12, mostrar_pasos: bool = False) -> Tuple[List[Numero], List[List[Numero]], List[Numero]]:
    """
    Resuelve A x = b por Eliminacion Gaussiana con pivoteo parcial.
    Devuelve (x, U, c) donde:
    - x: solucion
    - U: matriz triangular superior
    - c: vector b modificado
    """
    n = len(A)
    if any(len(fila) != n for fila in A):
        raise ValueError("La matriz A debe ser cuadrada")
    if len(b) != n:
        raise ValueError("Dimension de b incompatible con A")
    
    U = clonar_matriz(A)
    c = b[:]
    intercambios = 0
    
    # Eliminacion hacia adelante
    for i in range(n-1):
        # Pivoteo parcial: fila p con maximo |U[p][i]| para p en i..n-1
        p = i
        max_abs = abs(U[i][i])
        for l in range(i+1, n):
            if abs(U[l][i]) > max_abs:
                max_abs = abs(U[l][i])
                p = l
        
        if es_casi_cero(max_abs, tol):
            raise MatrizSingularError("Matriz singular o casi singular (pivote ~ 0).")
        
        if p != i:
            intercambiar_filas(U, c, i, p)
            intercambios += 1
        
        # Anular entradas debajo del pivote
        for j in range(i+1, n):
            factor = - U[j][i] / U[i][i]
            for k in range(i, n):
                U[j][k] += factor * U[i][k]
            c[j] += factor * c[i]
        
        if mostrar_pasos:
            from utils import mostrar_matriz, mostrar_vector
            print(f"Paso i={i}:\n" + mostrar_matriz(U))
            print("c = ", mostrar_vector(c))
    
    # Chequeo de determinante via producto de pivotes
    detU = producto_diagonal(U)
    detA = detU if intercambios % 2 == 0 else -detU
    
    if es_casi_cero(detA, tol):
        raise MatrizSingularError("Determinante ~ 0.")
    
    # Sustitucion hacia atras
    x = sustitucion_atras(U, c, tol=tol)
    
    return x, U, c