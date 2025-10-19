import numpy as np
import math
import matplotlib.pyplot as plt

def main():
    
    # Datos
    x_vals = [1.0, 1.2, 1.5, 2.0, 2.6, 2.9, 3.0]
    y_vals = [-0.236, 0.209, 0.853, 1.746, 2.231, 2.163, 2.110]
    
    print("\na) y b)")

    n = len(x_vals)
    
    # 1 coeficiente
    a11 = sum(math.sin(x_vals[k]) * math.sin(x_vals[k]) for k in range(n))
    
    # 2 coeficiente
    a12 = sum(math.sin(x_vals[k]) * math.cos(x_vals[k]) for k in range(n))
    
    # 3 coeficiente
    a21 = a12  # Esta simetrico aca
    
    # 4 coeficiente
    a22 = sum(math.cos(x_vals[k]) * math.cos(x_vals[k]) for k in range(n))
    
    b1 = sum(y_vals[k] * math.sin(x_vals[k]) for k in range(n))
    
    b2 = sum(y_vals[k] * math.cos(x_vals[k]) for k in range(n))
    
    A = np.array([[a11, a12], [a21, a22]])
    b = np.array([b1, b2])
    
    print("Matriz del sistema:")
    print(f"A = [[ {a11:.6f}, {a12:.6f} ]")
    print(f"     [ {a21:.6f}, {a22:.6f} ]]")
    
    print("\nVector de independientes:")
    print(f"b = [ {b1:.6f}, {b2:.6f} ]")
    
    print("\b)")
    
    # Resolver sistema usando eliminacion gaussiana
    def eliminacion_gaussiana(A, b):
        n = len(A)
        
        # Creo variables auxiliares para no modificar las originales
        A_copy = A.copy()
        b_copy = b.copy()
        
        # Eliminación hacia adelante
        for k in range(n):
            # Pivoteo parcial
            max_fila = k
            for i in range(k+1, n):
                if abs(A_copy[i, k]) > abs(A_copy[max_fila, k]):
                    max_fila = i
            
            # Intercambiar filas
            if max_fila != k:
                A_copy[[k, max_fila]] = A_copy[[max_fila, k]]
                b_copy[[k, max_fila]] = b_copy[[max_fila, k]]
            
            # Eliminación
            for i in range(k+1, n):
                if A_copy[k, k] != 0:
                    factor = A_copy[i, k] / A_copy[k, k]
                    A_copy[i, k:] -= factor * A_copy[k, k:]
                    b_copy[i] -= factor * b_copy[k]
        
        # Sustitución hacia atrás
        x = np.zeros(n)
        for i in range(n-1, -1, -1):
            x[i] = b_copy[i]
            for j in range(i+1, n):
                x[i] -= A_copy[i, j] * x[j]
            x[i] /= A_copy[i, i]
        
        return x
    
    # resolucion del sistema
    solucion = eliminacion_gaussiana(A, b)
    a, b = solucion
    
    print(f"solucion del sistema:")
    print(f"a = {a:.6f}")
    print(f"b = {b:.6f}")
    
    print(f"\nf(x) = {a:.6f}*sin(x) + {b:.6f}*cos(x)")
    
    y_est = [a * math.sin(x) + b * math.cos(x) for x in x_vals]
    residuos = [y_vals[i] - y_est[i] for i in range(n)]
    
    y_mean = sum(y_vals) / n
    
    St = sum((y_vals[i] - y_mean)**2 for i in range(n))
    
    Sr = sum(residuos[i]**2 for i in range(n))
    
    # Coeficiente de correlacion
    r_squared = 1 - Sr/St
    r = math.sqrt(r_squared)
    
    print(f"St = {St:.6f}")
    print(f"Sr = {Sr:.6f}")
    print(f"coeficiente de correlacion = {r:.6f}")

if __name__ == "__main__":
    main()