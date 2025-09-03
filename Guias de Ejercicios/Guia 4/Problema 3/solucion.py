import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=50):
    """Metodo de Gauss-Seidel simple"""
    n = len(b)
    x = x0.copy()
    
    for k in range(max_iter):
        x_old = x.copy()
        
        # Actualizar cada componente
        for i in range(n):
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma -= A[i,j] * x[j]
            x[i] = suma / A[i,i]
        
        # Calcular error
        error = np.linalg.norm(x - x_old)
        
        # Mostrar algunas iteraciones
        if k < 3 or error < tol:
            print(f"Iter {k+1}: x = {x}, error = {error:.2e}")
        
        if error < tol:
            return x, k+1
    
    return x, max_iter

def jacobi(A, b, x0, tol=1e-6, max_iter=50):
    """Metodo de Jacobi simple"""
    n = len(b)
    x = x0.copy()
    
    for k in range(max_iter):
        x_new = np.zeros(n)
        
        # Calcular nueva aproximacion
        for i in range(n):
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma -= A[i,j] * x[j]
            x_new[i] = suma / A[i,i]
        
        # Calcular error
        error = np.linalg.norm(x_new - x)
        x = x_new
        
        # Mostrar algunas iteraciones
        if k < 3 or error < tol:
            print(f"Iter {k+1}: x = {x}, error = {error:.2e}")
        
        if error < tol:
            return x, k+1
    
    return x, max_iter

# Sistema del problema
A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]], dtype=float)

b = np.array([11, 9, 11], dtype=float)
x0 = np.array([0, 0, 0], dtype=float)

print("PROBLEMA 3")
print("="*40)
print("Sistema Ax = b donde:")
print("A =", A)
print("b =", b)
print("x0 =", x0)

# Parte a) Gauss-Seidel
print("\na) GAUSS-SEIDEL")
print("-"*40)
sol_gs, iter_gs = gauss_seidel(A, b, x0)
print(f"\nSolucion: x = {sol_gs}")
print(f"Iteraciones: {iter_gs}")
print(f"Verificacion ||Ax-b|| = {np.linalg.norm(A@sol_gs - b):.2e}")

# Parte b) Comparacion con Jacobi  
print("\nb) JACOBI")
print("-"*40)
sol_j, iter_j = jacobi(A, b, x0)
print(f"\nSolucion: x = {sol_j}")
print(f"Iteraciones: {iter_j}")
print(f"Verificacion ||Ax-b|| = {np.linalg.norm(A@sol_j - b):.2e}")

# Comparacion
print("\nCOMPARACION:")
print(f"Gauss-Seidel: {iter_gs} iteraciones")
print(f"Jacobi: {iter_j} iteraciones")
print(f"Gauss-Seidel converge mas rapido: {iter_gs < iter_j}")