import numpy as np
import matplotlib.pyplot as plt

def regresion_cuadrados_minimos(x_datos, y_datos, grado=1):
    """
    Regresion por cuadrados minimos para cualquier grado polinomial
    """
    n = len(x_datos)
    p = grado
    
    # Construir matriz A y vector b
    A = np.zeros((p + 1, p + 1))
    b = np.zeros(p + 1)
    
    for l in range(p + 1):
        # Vector b
        suma = 0
        for i in range(n):
            suma += y_datos[i] * (x_datos[i] ** l)
        b[l] = suma
        
        # Matriz A
        for m in range(p + 1):
            suma = 0
            for i in range(n):
                suma += x_datos[i] ** (l + m)
            A[l, m] = suma
    
    # Resolver sistema con eliminacion gaussiana
    Ab = np.column_stack([A, b])  # Matriz aumentada
    
    # Eliminacion hacia adelante
    for i in range(p + 1):
        # Pivoteo
        max_row = i
        for k in range(i + 1, p + 1):
            if abs(Ab[k, i]) > abs(Ab[max_row, i]):
                max_row = k
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        # Eliminar
        for j in range(i + 1, p + 1):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    # Sustitucion hacia atras
    coef = np.zeros(p + 1)
    for i in range(p, -1, -1):
        suma = Ab[i, -1]
        for j in range(i + 1, p + 1):
            suma -= Ab[i, j] * coef[j]
        coef[i] = suma / Ab[i, i]
    
    # Calcular coeficiente de correlacion
    y_promedio = sum(y_datos) / n
    Sr = 0  # Error de regresion
    St = 0  # Error total
    
    for i in range(n):
        y_ajustado = sum(coef[j] * (x_datos[i] ** j) for j in range(p + 1))
        Sr += (y_ajustado - y_datos[i]) ** 2
        St += (y_datos[i] - y_promedio) ** 2
    
    r = np.sqrt((St - Sr) / St) if St > 0 else 0
    
    return coef, r

def main():
    # DATOS MODIFICABLES
    x = [0, 1, 2, 3, 4]
    y = [1, 1.5, 3.5, 3.9, 7.1]
    
    print("REGRESION POR CUADRADOS MINIMOS")
    print(f"Datos X: {x}")
    print(f"Datos Y: {y}")
    
    # Regresion lineal (grado 1)
    coef1, r1 = regresion_cuadrados_minimos(x, y, grado=1)
    print(f"\nLineal: y = {coef1[1]:.3f}x + {coef1[0]:.3f}")
    print(f"r = {r1:.4f}")
    
    # Regresion cuadratica (grado 2)
    coef2, r2 = regresion_cuadrados_minimos(x, y, grado=2)
    print(f"\nCuadratica: y = {coef2[2]:.3f}x^2 + {coef2[1]:.3f}x + {coef2[0]:.3f}")
    print(f"r = {r2:.4f}")
    
    # Graficar
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='red', s=50, label='Datos')
    
    x_plot = np.linspace(min(x), max(x), 100)
    
    # Curva lineal
    y_lin = coef1[0] + coef1[1] * x_plot
    plt.plot(x_plot, y_lin, 'b-', label=f'Lineal (r={r1:.3f})')
    
    # Curva cuadratica
    y_quad = coef2[0] + coef2[1] * x_plot + coef2[2] * x_plot**2
    plt.plot(x_plot, y_quad, 'g-', label=f'Cuadratica (r={r2:.3f})')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.title('Ajuste por Cuadrados Minimos')
    
    # Guardar grafico como PNG
    plt.savefig('regresion_cuadrados_minimos.png', dpi=150, bbox_inches='tight')
    print("\nGrafico guardado como 'regresion_cuadrados_minimos.png'")
    
    plt.show()

if __name__ == "__main__":
    main()