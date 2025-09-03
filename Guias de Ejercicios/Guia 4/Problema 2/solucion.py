import math

def gauss_seidel(A, b, x0, tol=1e-11, max_iter=100):
    """Metodo de Gauss-Seidel simple"""
    n = len(b)
    x = x0[:]
    
    for k in range(max_iter):
        x_old = x[:]
        
        # Actualizar cada componente
        for i in range(n):
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma -= A[i][j] * x[j]
            x[i] = suma / A[i][i]
        
        # Calcular error
        error = math.sqrt(sum((x[i] - x_old[i])**2 for i in range(n)))
        
        if error < tol:
            return x, k+1
    
    return x, max_iter

# PARTE (a)
print("Parte (a):")
A1 = [[3, 1, 1],
      [2, 6, 1],
      [1, 1, 4]]
b1 = [5, 9, 6]
x0 = [0, 0, 0]

sol_a, iter_a = gauss_seidel(A1, b1, x0, tol=1e-11)
print(f"Solucion: x1={sol_a[0]:.6f}, x2={sol_a[1]:.6f}, x3={sol_a[2]:.6f}")
print(f"Iteraciones necesarias: {iter_a}")

# PARTE (b)
print("\nParte (b):")
A2 = [[5, 7, 6, 5],
      [7, 10, 8, 7],
      [6, 8, 10, 9],
      [5, 7, 9, 10]]
b2 = [23, 32, 33, 31]
x0 = [0, 0, 0, 0]

# Solo 7 iteraciones
x = x0[:]
print("Iteracion 0:", [0, 0, 0, 0])

for k in range(7):
    # x1
    x[0] = (b2[0] - A2[0][1]*x[1] - A2[0][2]*x[2] - A2[0][3]*x[3]) / A2[0][0]
    # x2
    x[1] = (b2[1] - A2[1][0]*x[0] - A2[1][2]*x[2] - A2[1][3]*x[3]) / A2[1][1]
    # x3
    x[2] = (b2[2] - A2[2][0]*x[0] - A2[2][1]*x[1] - A2[2][3]*x[3]) / A2[2][2]
    # x4
    x[3] = (b2[3] - A2[3][0]*x[0] - A2[3][1]*x[1] - A2[3][2]*x[2]) / A2[3][3]
    
    print(f"Iteracion {k+1}: [{x[0]:.6f}, {x[1]:.6f}, {x[2]:.6f}, {x[3]:.6f}]")

print(f"\nSolucion despues de 7 iteraciones: x={x}")