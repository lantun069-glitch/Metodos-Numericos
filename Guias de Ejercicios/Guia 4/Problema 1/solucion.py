import numpy as np

def jacobi(A, b, tol=1e-6, max_iter=100):
    """Metodo de Jacobi para resolver Ax = b"""
    n = len(b)
    x = np.zeros(n)
    x_nuevo = np.zeros(n)
    
    for k in range(max_iter):
        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    suma += A[i,j] * x[j]
            x_nuevo[i] = (b[i] - suma) / A[i,i]
        
        # Calcular error
        error = np.linalg.norm(x_nuevo - x)
        if error < tol:
            print(f"Jacobi converge en {k+1} iteraciones")
            return x_nuevo
        
        x = x_nuevo.copy()
    
    print("Jacobi no converge")
    return None

def gauss_seidel(A, b, tol=1e-6, max_iter=100):
    """Metodo de Gauss-Seidel para resolver Ax = b"""
    n = len(b)
    x = np.zeros(n)
    
    for k in range(max_iter):
        x_ant = x.copy()
        
        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    suma += A[i,j] * x[j]
            x[i] = (b[i] - suma) / A[i,i]
        
        # Calcular error
        error = np.linalg.norm(x - x_ant)
        if error < tol:
            print(f"Gauss-Seidel converge en {k+1} iteraciones")
            return x
    
    print("Gauss-Seidel no converge")
    return None

def main():
    print("PROBLEMA 1: Metodos de Jacobi y Gauss-Seidel")
    print("="*50)
    
    # Sistema original (1)
    print("\nSISTEMA (1) - Original:")
    print("4x - y + z = 7")
    print("4x - 8y + z = -21")
    print("-2x + y + 5z = 15")
    
    A1 = np.array([[4, -1, 1],
                   [4, -8, 1],
                   [-2, 1, 5]], dtype=float)
    b1 = np.array([7, -21, 15], dtype=float)
    
    print("\nResolviendo con Jacobi:")
    sol_j = jacobi(A1, b1)
    if sol_j is not None:
        print(f"Solucion: x={sol_j[0]:.1f}, y={sol_j[1]:.1f}, z={sol_j[2]:.1f}")
    
    print("\nResolviendo con Gauss-Seidel:")
    sol_gs = gauss_seidel(A1, b1)
    if sol_gs is not None:
        print(f"Solucion: x={sol_gs[0]:.1f}, y={sol_gs[1]:.1f}, z={sol_gs[2]:.1f}")
    
    # Sistema reordenado (2) - intercambiando filas 1 y 3
    print("\n" + "="*50)
    print("\nSISTEMA (2) - Intercambiando filas 1 y 3:")
    print("-2x + y + 5z = 15")
    print("4x - 8y + z = -21")  
    print("4x - y + z = 7")
    
    A2 = np.array([[-2, 1, 5],
                   [4, -8, 1],
                   [4, -1, 1]], dtype=float)
    b2 = np.array([15, -21, 7], dtype=float)
    
    print("\nResolviendo con Jacobi:")
    sol_j2 = jacobi(A2, b2, max_iter=20)  # Limitar iteraciones para ver divergencia
    
    print("\nResolviendo con Gauss-Seidel:")
    sol_gs2 = gauss_seidel(A2, b2, max_iter=20)
    
    print("\n" + "="*50)
    print("RESPUESTA FINAL:")
    print(f"Solucion del sistema: x = 2, y = 4, z = 3")
    print("\nEl sistema (2) DIVERGE porque al reordenar las filas")
    print("la matriz pierde la propiedad de diagonal dominante.")

if __name__ == "__main__":
    main()