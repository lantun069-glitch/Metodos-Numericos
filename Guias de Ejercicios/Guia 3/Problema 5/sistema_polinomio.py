from typing import List, Tuple
import math

def calcular_norma_frobenius(A: List[List[float]]) -> float:
    """Calcula la norma de Frobenius de una matriz."""
    suma = 0.0
    for fila in A:
        for valor in fila:
            suma += valor * valor
    return math.sqrt(suma)

def calcular_determinante(A: List[List[float]]) -> float:
    """Calcula el determinante por eliminacion gaussiana."""
    n = len(A)
    U = [fila[:] for fila in A]
    det = 1.0
    intercambios = 0
    
    for i in range(n-1):
        p = i
        max_abs = abs(U[i][i])
        for j in range(i+1, n):
            if abs(U[j][i]) > max_abs:
                max_abs = abs(U[j][i])
                p = j
        
        if abs(max_abs) < 1e-15:
            return 0.0
            
        if p != i:
            U[i], U[p] = U[p], U[i]
            intercambios += 1
            
        for j in range(i+1, n):
            factor = U[j][i] / U[i][i]
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]
    
    for i in range(n):
        det *= U[i][i]
    
    return det if intercambios % 2 == 0 else -det

def sustitucion_atras(U: List[List[float]], y: List[float]) -> List[float]:
    """Resuelve Ux = y por sustitucion hacia atras."""
    n = len(U)
    x = [0.0] * n
    
    for i in range(n-1, -1, -1):
        s = y[i]
        for j in range(i+1, n):
            s -= U[i][j] * x[j]
        x[i] = s / U[i][i]
    
    return x

def eliminacion_gaussiana(A: List[List[float]], b: List[float]) -> List[float]:
    """Resuelve Ax = b por eliminacion gaussiana con pivoteo parcial."""
    n = len(A)
    U = [fila[:] for fila in A]
    c = b[:]
    
    for i in range(n-1):
        p = i
        max_abs = abs(U[i][i])
        for j in range(i+1, n):
            if abs(U[j][i]) > max_abs:
                max_abs = abs(U[j][i])
                p = j
        
        if p != i:
            U[i], U[p] = U[p], U[i]
            c[i], c[p] = c[p], c[i]
        
        for j in range(i+1, n):
            if abs(U[i][i]) < 1e-15:
                raise ValueError("Matriz singular")
            factor = U[j][i] / U[i][i]
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]
            c[j] -= factor * c[i]
    
    return sustitucion_atras(U, c)