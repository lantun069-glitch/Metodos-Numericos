import numpy as np
from typing import Tuple, Optional

def metodo_jacobi(A: np.ndarray, b: np.ndarray, tolerancia: float = 1e-6, 
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
    x_viejo = np.zeros(n)
    x_nuevo = np.zeros(n)
    error_viejo = 1000
    iteraciones = 0
    
    # Proceso iterativo
    while iteraciones < max_iter:
        iteraciones += 1
        
        # Calcular nueva aproximacion
        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    suma += A[i, j] * x_viejo[j]
            
            x_nuevo[i] = (b[i] - suma) / A[i, i]
        
        # Calcular error
        error = np.sqrt(np.sum((x_nuevo - x_viejo)**2))
        
        # Verificar convergencia
        if error > error_viejo:
            print("El metodo no converge")
            return None, iteraciones, error
        
        # Verificar tolerancia
        if error < tolerancia:
            return x_nuevo, iteraciones, error
        
        # Actualizar para siguiente iteracion
        x_viejo = x_nuevo.copy()
        error_viejo = error
    
    print("Se alcanzo el numero maximo de iteraciones")
    return x_nuevo, iteraciones, error

# Ejemplo de uso
if __name__ == "__main__":
    # Sistema de ejemplo del documento
    A = np.array([[2, 1], 
                  [1, -3]], dtype=float)
    b = np.array([3, -2], dtype=float)
    
    solucion, iter, err = metodo_jacobi(A, b, tolerancia=0.01)
    if solucion is not None:
        print(f"Solucion: {solucion}")
        print(f"Iteraciones: {iter}")
        print(f"Error: {err}")
