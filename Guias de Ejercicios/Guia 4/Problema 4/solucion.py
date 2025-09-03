import numpy as np

def resolver_sistema():
    # Construir sistema de 50x50 con estructura de banda
    n = 50
    A = np.zeros((n, n))
    b = np.ones(n) * 5.0
    
    # Llenar matriz banda: x[i-2] - 2x[i-1] + 12x[i] - 2x[i+1] + x[i+2] = 5
    for i in range(n):
        A[i, i] = 12.0  # Diagonal principal
        if i > 0: A[i, i-1] = -2.0
        if i < n-1: A[i, i+1] = -2.0
        if i > 1: A[i, i-2] = 1.0
        if i < n-2: A[i, i+2] = 1.0
    
    # Gauss-Seidel
    x = np.zeros(n)
    tol = 1e-6
    max_iter = 1000
    
    for iter in range(max_iter):
        x_ant = x.copy()
        
        # Actualizar cada componente
        for i in range(n):
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma -= A[i, j] * x[j]
            x[i] = suma / A[i, i]
        
        # Verificar convergencia
        error = np.max(np.abs(x - x_ant))
        if error < tol:
            print(f"Convergencia en {iter+1} iteraciones")
            print(f"Error: {error:.2e}")
            break
    
    # Verificar solucion
    residuo = np.linalg.norm(A @ x - b)
    print(f"||Ax - b|| = {residuo:.2e}")
    
    # Mostrar algunos valores
    print("\nPrimeros valores de x:")
    for i in range(5):
        print(f"x[{i}] = {x[i]:.6f}")
    
    print("\nUltimos valores de x:")
    for i in range(n-5, n):
        print(f"x[{i}] = {x[i]:.6f}")
    
    return x

if __name__ == "__main__":
    print("RESOLUCION SISTEMA BANDA CON GAUSS-SEIDEL")
    print("-" * 40)
    solucion = resolver_sistema()