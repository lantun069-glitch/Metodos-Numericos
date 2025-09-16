import numpy as np
import matplotlib.pyplot as plt

def spline_cubica(x_datos, y_datos):
    """
    Calcula los coeficientes para spline cubica natural
    Cada tramo: Sk(x) = ak + bk*(x-xk) + ck*(x-xk)^2 + dk*(x-xk)^3
    """
    n = len(x_datos)
    
    # Paso 1: Calcular las diferencias h
    h = np.zeros(n-1)
    for i in range(n-1):
        h[i] = x_datos[i+1] - x_datos[i]
    
    # Paso 2: Sistema tridiagonal para las segundas derivadas (M)
    # Construir matriz A y vector b
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    # Condiciones de frontera natural: M0 = 0, Mn-1 = 0
    A[0, 0] = 1
    A[n-1, n-1] = 1
    
    # Ecuaciones para nodos internos
    for i in range(1, n-1):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        
        # Lado derecho
        b[i] = 6 * ((y_datos[i+1] - y_datos[i])/h[i] - 
                    (y_datos[i] - y_datos[i-1])/h[i-1])
    
    # Resolver sistema para obtener M (segundas derivadas)
    M = np.linalg.solve(A, b)
    
    # Paso 3: Calcular coeficientes de cada polinomio cubico
    coeficientes = []
    for i in range(n-1):
        # Coeficientes para el intervalo i
        ai = y_datos[i]
        bi = (y_datos[i+1] - y_datos[i])/h[i] - h[i]*(2*M[i] + M[i+1])/6
        ci = M[i]/2
        di = (M[i+1] - M[i])/(6*h[i])
        
        coeficientes.append([ai, bi, ci, di])
    
    return np.array(coeficientes)

def evaluar_spline_cubica(x, x_datos, coeficientes):
    """
    Evalua el spline cubico en el punto x
    """
    n = len(x_datos)
    
    # Encontrar el intervalo correcto
    if x <= x_datos[0]:
        k = 0
    elif x >= x_datos[-1]:
        k = n - 2
    else:
        for i in range(n-1):
            if x_datos[i] <= x <= x_datos[i+1]:
                k = i
                break
    
    # Evaluar el polinomio cubico en el intervalo k
    dx = x - x_datos[k]
    ak, bk, ck, dk = coeficientes[k]
    
    resultado = ak + bk*dx + ck*dx**2 + dk*dx**3
    
    return resultado

# ==============================================================
# EJEMPLO MODIFICABLE - CAMBIAR ESTOS VALORES LOS DATOS DADOS
# ==============================================================

# Datos de entrada (puntos conocidos)
x_datos = np.array([0.0, 1.0, 2.5, 4.0, 5.0, 6.0])  # Valores de x
y_datos = np.array([2.5, 1.0, 0.5, 1.5, 2.0, 1.2])  # Valores de y

# Punto donde quieres interpolar
x_interpolar = 3.2

# ==============================================================
# CALCULO Y VISUALIZACION (no necesitas modificar esta parte)
# ==============================================================

# Calcular coeficientes del spline cubico
coeficientes = spline_cubica(x_datos, y_datos)

# Interpolar en el punto deseado
valor_interpolado = evaluar_spline_cubica(x_interpolar, x_datos, coeficientes)
print(f"Valor interpolado en x = {x_interpolar}: y = {valor_interpolado:.4f}")

# Mostrar los polinomios de cada tramo
print("\nPolinomios cubicos por tramos:")
for i in range(len(x_datos)-1):
    ak, bk, ck, dk = coeficientes[i]
    print(f"S{i}(x) = {ak:.4f} + {bk:.4f}(x-{x_datos[i]:.1f}) + {ck:.4f}(x-{x_datos[i]:.1f})^2 + {dk:.4f}(x-{x_datos[i]:.1f})^3")
    print(f"        Valido en [{x_datos[i]:.1f}, {x_datos[i+1]:.1f}]")

# Crear puntos para graficar la curva suave
x_curva = np.linspace(x_datos[0], x_datos[-1], 500)
y_curva = [evaluar_spline_cubica(x, x_datos, coeficientes) for x in x_curva]

# Crear el grafico
plt.figure(figsize=(10, 6))

# Graficar spline cubico
plt.plot(x_curva, y_curva, 'b-', linewidth=2, label='Spline Cubica')

# Graficar puntos originales
plt.plot(x_datos, y_datos, 'ro', markersize=8, label='Puntos datos')

# Graficar punto interpolado
plt.plot(x_interpolar, valor_interpolado, 'g*', markersize=15, 
         label=f'Interpolado: ({x_interpolar:.2f}, {valor_interpolado:.2f})')

# Configurar el grafico
plt.grid(True, alpha=0.3)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Interpolacion con Spline Cubica Natural', fontsize=14, fontweight='bold')
plt.legend(loc='best', fontsize=10)

# Agregar anotacion con informacion
info_text = f'Numero de puntos: {len(x_datos)}\nNumero de tramos: {len(x_datos)-1}'
plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes, 
         fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Ajustar layout y guardar
plt.tight_layout()
plt.savefig('spline_cubica_interpolacion.png', dpi=150, bbox_inches='tight')
print("\nGrafico guardado como 'spline_cubica_interpolacion.png' en el directorio actual")

# Mostrar el grafico
plt.show()