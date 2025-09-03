import numpy as np
from typing import Tuple, Optional

def metodo_relajacion(A: np.ndarray, b: np.ndarray, omega: float = 1.0,
                     tolerancia: float = 1e-6, max_iter: int = 1000) -> Tuple[Optional[np.ndarray], int, float]:
    n = len(b)
    
    # Validar parametro omega
    if omega <= 0 or omega >= 2:
        print(f"Parametro omega = {omega} fuera de rango (0, 2)")
        return None, 0, float('inf')
    
    # Verificar diagonal dominante (recomendado pero no estrictamente necesario)
    es_diagonal_dominante = True
    for i in range(n):
        suma = 0
        for j in range(n):
            if i != j:
                suma += abs(A[i, j])
        
        if abs(A[i, i]) <= suma:
            es_diagonal_dominante = False
            print(f"Advertencia: La matriz no es diagonalmente dominante en fila {i}")
    
    if not es_diagonal_dominante and omega >= 1:
        print("Considere usar sub-relajacion (omega < 1) para mejorar convergencia")
    
    # Inicializar vector solucion
    x = np.zeros(n)
    x_anterior = np.zeros(n)
    error_viejo = 1000
    iteraciones = 0
    
    # Proceso iterativo
    while iteraciones < max_iter:
        iteraciones += 1
        x_anterior = x.copy()
        
        # Calcular nueva aproximacion con relajacion
        for i in range(n):
            suma = 0
            # Usar valores ya actualizados (j < i)
            for j in range(i):
                suma += A[i, j] * x[j]
            # Usar valores anteriores (j > i)  
            for j in range(i + 1, n):
                suma += A[i, j] * x[j]
            
            # Aplicar formula de relajacion
            x_gauss_seidel = (b[i] - suma) / A[i, i]
            x[i] = omega * x_gauss_seidel + (1 - omega) * x_anterior[i]
        
        # Calcular error
        error = np.sqrt(np.sum((x - x_anterior)**2))
        
        # Verificar convergencia
        if error > error_viejo * 1.5:  # Permitir pequeñas fluctuaciones
            print(f"Advertencia: El metodo puede no estar convergiendo (iter={iteraciones})")
        
        # Verificar tolerancia
        if error < tolerancia:
            print(f"Convergencia alcanzada con omega = {omega}")
            return x, iteraciones, error
        
        error_viejo = error
    
    print("Se alcanzo el numero maximo de iteraciones")
    return x, iteraciones, error

# Funcion auxiliar para encontrar omega optimo
def encontrar_omega_optimo(A: np.ndarray, b: np.ndarray, 
                          omega_min: float = 0.1, omega_max: float = 1.9,
                          paso: float = 0.1) -> float:
    """
    Encuentra empiricamente el valor de omega que minimiza las iteraciones
    """
    mejor_omega = 1.0
    min_iteraciones = float('inf')
    
    omega = omega_min
    while omega <= omega_max:
        sol, iter, err = metodo_relajacion(A, b, omega, tolerancia=1e-6)
        if sol is not None and iter < min_iteraciones:
            min_iteraciones = iter
            mejor_omega = omega
        omega += paso
    
    return mejor_omega

# Ejemplo de uso
if __name__ == "__main__":
    # Sistema de ejemplo
    A = np.array([[4, -1, 0], 
                  [-1, 4, -1],
                  [0, -1, 3]], dtype=float)
    b = np.array([15, 10, 10], dtype=float)
    
    print("=== Gauss-Seidel estandar (omega = 1.0) ===")
    sol1, iter1, err1 = metodo_relajacion(A, b, omega=1.0)
    if sol1 is not None:
        print(f"Solucion: {sol1}")
        print(f"Iteraciones: {iter1}")
        
    print("\n=== Sobre-relajacion (omega = 1.5) ===")
    sol2, iter2, err2 = metodo_relajacion(A, b, omega=1.5)
    if sol2 is not None:
        print(f"Solucion: {sol2}")
        print(f"Iteraciones: {iter2}")
    
    print("\n=== Busqueda de omega optimo ===")
    omega_opt = encontrar_omega_optimo(A, b)
    print(f"Omega optimo encontrado: {omega_opt}")
    
    sol3, iter3, err3 = metodo_relajacion(A, b, omega=omega_opt)
    if sol3 is not None:
        print(f"Solucion: {sol3}")
        print(f"Iteraciones: {iter3}")
