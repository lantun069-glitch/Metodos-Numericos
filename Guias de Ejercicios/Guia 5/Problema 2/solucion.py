import math
import matplotlib.pyplot as plt
import numpy as np

def interpolacion_lagrange(puntos_x, puntos_y, x_eval):
    """Interpolacion de Lagrange"""
    n = len(puntos_x)
    suma = 0.0
    for i in range(n):
        producto = 1.0
        for k in range(n):
            if k != i:
                producto *= (x_eval - puntos_x[k]) / (puntos_x[i] - puntos_x[k])
        suma += puntos_y[i] * producto
    return suma

# Funciones a interpolar
def f1(x):
    return math.exp(-x**2)

def f2(x):
    return 4*x**3 - 3*x**2 + 2

def f3(x):
    return x**7

# INCISO 1: f(x) = exp(-x^2)
print("INCISO 1: f(x) = exp(-x^2)")
print("-"*40)

plt.figure(figsize=(12, 8))
for idx, n in enumerate([2, 4, 6, 8]):
    plt.subplot(2, 2, idx+1)
    
    # Puntos de interpolacion uniformes
    puntos_x = np.linspace(-2, 2, n+1)
    puntos_y = [f1(x) for x in puntos_x]
    
    # Graficar funcion exacta y polinomio
    x_plot = np.linspace(-2, 2, 200)
    y_exacta = [f1(x) for x in x_plot]
    y_interp = [interpolacion_lagrange(puntos_x, puntos_y, x) for x in x_plot]
    
    plt.plot(x_plot, y_exacta, 'b-', label='Exacta')
    plt.plot(x_plot, y_interp, 'r--', label=f'P_{n}(x)')
    plt.plot(puntos_x, puntos_y, 'ko')
    
    # Calcular error en puntos de interpolacion
    print(f"n = {n}:")
    for xi, yi in zip(puntos_x, puntos_y):
        p_xi = interpolacion_lagrange(puntos_x, puntos_y, xi)
        error = abs(p_xi - yi)
        print(f"  x={xi:5.2f}: error = {error:.2e}")
    
    plt.title(f'n = {n}')
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('inciso1.png')

# INCISO 2: f(x) = 4x^3 - 3x^2 + 2
print("\nINCISO 2: f(x) = 4x^3 - 3x^2 + 2")
print("-"*40)

plt.figure(figsize=(10, 6))
x_plot = np.linspace(-1.5, 2.5, 300)

for n in [1, 2, 3]:
    # Puntos de interpolacion en [-1, 2]
    puntos_x = np.linspace(-1, 2, n+1)
    puntos_y = [f2(x) for x in puntos_x]
    
    # Evaluar polinomio
    y_interp = [interpolacion_lagrange(puntos_x, puntos_y, x) for x in x_plot]
    
    plt.plot(x_plot, y_interp, label=f'P_{n}(x)')
    
    # Error dentro y fuera del rango
    x_dentro = x_plot[(x_plot >= -1) & (x_plot <= 2)]
    error_dentro = max([abs(interpolacion_lagrange(puntos_x, puntos_y, x) - f2(x)) 
                       for x in x_dentro])
    print(f"n = {n}: Error max en [-1,2] = {error_dentro:.2e}")

# Funcion exacta
y_exacta = [f2(x) for x in x_plot]
plt.plot(x_plot, y_exacta, 'k-', linewidth=2, label='Exacta')
plt.axvspan(-1, 2, alpha=0.1, color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomios interpoladores')
plt.legend()
plt.grid(True)
plt.savefig('inciso2.png')

# INCISO 3: f(x) = x^7
print("\nINCISO 3: f(x) = x^7")
print("-"*40)

plt.figure(figsize=(10, 6))
x_plot = np.linspace(-1.2, 1.2, 300)
y_exacta = [f3(x) for x in x_plot]

for n in [3, 5, 7]:
    # Puntos de interpolacion en [-1, 1]
    puntos_x = np.linspace(-1, 1, n+1)
    puntos_y = [f3(x) for x in puntos_x]
    
    # Evaluar polinomio
    y_interp = [interpolacion_lagrange(puntos_x, puntos_y, x) for x in x_plot]
    
    plt.plot(x_plot, y_interp, label=f'P_{n}(x)', alpha=0.7)
    
    # Verificar error
    error = max([abs(interpolacion_lagrange(puntos_x, puntos_y, xi) - yi) 
                for xi, yi in zip(puntos_x, puntos_y)])
    print(f"n = {n}: Error en puntos = {error:.2e}")

plt.plot(x_plot, y_exacta, 'k-', linewidth=2, label='x^7 exacta')
plt.axvspan(-1, 1, alpha=0.1, color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolacion de x^7')
plt.legend()
plt.grid(True)
plt.savefig('inciso3.png')

# ANALISIS FUERA DEL RANGO
print("\nANALISIS: Comportamiento fuera del rango")
print("-"*40)

plt.figure(figsize=(10, 6))
n = 8
puntos_x = np.linspace(-2, 2, n+1)
puntos_y = [f1(x) for x in puntos_x]

x_ext = np.linspace(-3, 3, 400)
y_exacta = [f1(x) for x in x_ext]
y_interp = [interpolacion_lagrange(puntos_x, puntos_y, x) for x in x_ext]

plt.plot(x_ext, y_exacta, 'b-', label='Exacta')
plt.plot(x_ext, y_interp, 'r--', label=f'P_{n}(x)')
plt.axvspan(-2, 2, alpha=0.2, color='green', label='Rango interp.')
plt.plot(puntos_x, puntos_y, 'ko')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Extrapolacion: comportamiento fuera del rango')
plt.legend()
plt.grid(True)
plt.ylim(-1, 2)
plt.savefig('extrapolacion.png')

print("\nCONCLUSION: El polinomio oscila fuera del rango de interpolacion")
print("Graficos guardados: inciso1.png, inciso2.png, inciso3.png, extrapolacion.png")
plt.show()