import numpy as np
from typing import Tuple, Optional

def metodo_gauss_seidel(A: np.ndarray, b: np.ndarray, tolerancia: float = 1e-6,
                        max_iter: int = 1000) -> Tuple[Optional[np.ndarray], int, float]:
    n = len(b)
    
    # Verificar si la matriz es diagonalmente dominante
    for i in range(n):
        suma = 0
        for j in range(n):
            if i != j:
                suma += abs(A[i, j])
        
        if abs(A[i, i]) <= suma:
            print("La matriz no es diagonalmente dominante")
            print(f"Fila {i}: |{A[i,i]}| <= {suma}")
            return None, 0, float('inf')
    
    # Inicializar vector solucion
    x = np.zeros(n)
    x_anterior = np.zeros(n)
    error_viejo = 1000
    iteraciones = 0
    
    # Proceso iterativo
    while iteraciones < max_iter:
        iteraciones += 1
        x_anterior = x.copy()
        
        # Calcular nueva aproximacion usando valores actualizados
        for i in range(n):
            suma = 0
            # Usar valores ya actualizados (j < i)
            for j in range(i):
                suma += A[i, j] * x[j]
            # Usar valores anteriores (j > i)
            for j in range(i + 1, n):
                suma += A[i, j] * x[j]
            
            x[i] = (b[i] - suma) / A[i, i]
        
        # Calcular error
        error = np.sqrt(np.sum((x - x_anterior)**2))
        
        # Verificar convergencia
        if error > error_viejo:
            print("El metodo no converge")
            return None, iteraciones, error
        
        # Verificar tolerancia
        if error < tolerancia:
            return x, iteraciones, error
        
        error_viejo = error
    
    print("Se alcanzo el numero maximo de iteraciones")
    return x, iteraciones, error

# Ejemplo de uso
if __name__ == "__main__":
    # Sistema de ejemplo
    A = np.array([[2, 1], 
                  [1, -3]], dtype=float)
    b = np.array([3, -2], dtype=float)
    
    solucion, iter, err = metodo_gauss_seidel(A, b, tolerancia=0.01)
    if solucion is not None:
        print(f"Solucion: {solucion}")
        print(f"Iteraciones: {iter}")
        print(f"Error: {err}")
