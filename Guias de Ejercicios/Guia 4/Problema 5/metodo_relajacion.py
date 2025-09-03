import numpy as np
from typing import Tuple, Optional

def metodo_relajacion(A: np.ndarray, b: np.ndarray, x_inicial: np.ndarray, 
                      omega: float = 1.0, tolerancia: float = 1e-6, 
                      max_iter: int = 1000) -> Tuple[Optional[np.ndarray], int, float]:
    """
    Metodo de Gauss-Seidel con relajacion para resolver Ax = b
    """
    n = len(b)
    
    # Verificar si la matriz es diagonalmente dominante
    es_diagonal_dominante = True
    for i in range(n):
        suma = 0
        for j in range(n):
            if i != j:
                suma += abs(A[i, j])
        if abs(A[i, i]) <= suma:
            es_diagonal_dominante = False
            print(f"Fila {i}: |{A[i,i]}| = {abs(A[i,i]):.4f} <= suma = {suma:.4f}")
    
    if es_diagonal_dominante:
        print("La matriz ES diagonalmente dominante")
    else:
        print("La matriz NO es diagonalmente dominante")
    
    # Inicializar con x_inicial proporcionado
    x = x_inicial.copy()
    x_anterior = x.copy()
    iteraciones = 0
    
    # Proceso iterativo
    while iteraciones < max_iter:
        iteraciones += 1
        x_anterior = x.copy()
        
        # Aplicar formula de relajacion para cada componente
        for i in range(n):
            suma = 0
            # Usar valores ya actualizados (j < i)
            for j in range(i):
                suma += A[i, j] * x[j]
            # Usar valores anteriores (j > i)  
            for j in range(i + 1, n):
                suma += A[i, j] * x[j]
            
            # Formula de relajacion
            x_gauss_seidel = (b[i] - suma) / A[i, i]
            x[i] = omega * x_gauss_seidel + (1 - omega) * x_anterior[i]
        
        # Calcular error
        error = np.sqrt(np.sum((x - x_anterior)**2))
        
        # Verificar convergencia
        if error < tolerancia:
            return x, iteraciones, error
    
    print(f"Se alcanzo el numero maximo de iteraciones ({max_iter})")
    return x, iteraciones, error