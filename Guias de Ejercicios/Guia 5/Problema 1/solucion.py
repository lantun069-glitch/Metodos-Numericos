import numpy as np
import matplotlib.pyplot as plt

def coeficiente_lagrange(x, nodos, k):
    """Calcula el coeficiente de Lagrange C_N,k(x)"""
    n = len(nodos)
    producto = 1.0
    for j in range(n):
        if j != k:
            producto *= (x - nodos[j]) / (nodos[k] - nodos[j])
    return producto

def polinomio_lagrange(x, nodos, valores):
    """Calcula P_N(x) = suma de f(x_k) * C_N,k(x)"""
    suma = 0
    for k in range(len(nodos)):
        suma += valores[k] * coeficiente_lagrange(x, nodos, k)
    return suma

def verificar_propiedades():
    """Verifica las propiedades de los coeficientes de Lagrange"""
    # Nodos dados en el problema
    nodos = [1.0, 2.0, 2.5]
    n = len(nodos)
    
    print("VERIFICACION DE PROPIEDADES")
    print("="*40)
    
    # Verificar C_N,k(x_k) = 1 y C_N,k(x_j) = 0 para j != k
    print("\n1. C_N,k(x_k) = 1 y C_N,k(x_j) = 0:")
    for k in range(n):
        for j in range(n):
            valor = coeficiente_lagrange(nodos[j], nodos, k)
            esperado = 1.0 if j == k else 0.0
            print(f"   C_{n-1},{k}({nodos[j]}) = {valor:.6f} (esperado: {esperado})")
    
    # Verificar suma = 1
    print("\n2. Suma de C_N,k(x) = 1:")
    x_test = 1.75  # Punto de prueba
    suma = sum(coeficiente_lagrange(x_test, nodos, k) for k in range(n))
    print(f"   En x = {x_test}: suma = {suma:.6f}")
    
    # Graficar coeficientes
    graficar_coeficientes(nodos)

def graficar_coeficientes(nodos):
    """Grafica los coeficientes de Lagrange"""
    x = np.linspace(0.5, 3.0, 300)
    n = len(nodos)
    
    plt.figure(figsize=(10, 6))
    
    # Graficar cada coeficiente
    for k in range(n):
        y = [coeficiente_lagrange(xi, nodos, k) for xi in x]
        plt.plot(x, y, label=f'$C_{{2,{k}}}(x)$', linewidth=2)
    
    # Marcar los nodos
    for k in range(n):
        for j in range(n):
            valor = coeficiente_lagrange(nodos[j], nodos, k)
            if j == k:
                plt.plot(nodos[j], valor, 'o', markersize=8)
    
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axhline(y=1, color='k', linestyle='--', alpha=0.3)
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('$C_{N,k}(x)$')
    plt.title('Coeficientes de Lagrange cuadraticos')
    plt.legend()
    plt.savefig('coeficientes.png')
    print("\nGrafico guardado: coeficientes.png")

def analizar_error():
    """Analiza el error de interpolacion"""
    nodos = [1.0, 2.0, 2.5]
    
    # Funcion de prueba
    def f(x):
        return np.sin(x) + x/2
    
    # Valores en los nodos
    valores = [f(xi) for xi in nodos]
    
    # Verificar e(x_k) = 0
    print("\n\nERROR EN LOS NODOS")
    print("="*40)
    for k, xk in enumerate(nodos):
        p_xk = polinomio_lagrange(xk, nodos, valores)
        error = abs(f(xk) - p_xk)
        print(f"e(x_{k}) = |f({xk}) - P_N({xk})| = {error:.2e}")
    
    # Graficar funcion, interpolacion y error
    graficar_interpolacion(nodos, f)

def graficar_interpolacion(nodos, f):
    """Grafica la interpolacion y el error"""
    valores = [f(xi) for xi in nodos]
    x = np.linspace(0.5, 3.0, 300)
    
    # Calcular funciones
    y_real = [f(xi) for xi in x]
    y_interp = [polinomio_lagrange(xi, nodos, valores) for xi in x]
    error = [abs(yr - yi) for yr, yi in zip(y_real, y_interp)]
    
    # Crear graficos
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Grafico 1: Funcion e interpolacion
    ax1.plot(x, y_real, 'b-', label='f(x)', linewidth=2)
    ax1.plot(x, y_interp, 'r--', label='$P_N(x)$', linewidth=2)
    ax1.plot(nodos, valores, 'ko', markersize=8, label='Nodos')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Interpolacion de Lagrange')
    ax1.legend()
    
    # Grafico 2: Error
    ax2.semilogy(x, error, 'g-', linewidth=2)
    ax2.set_xlabel('x')
    ax2.set_ylabel('|f(x) - $P_N(x)$|')
    ax2.set_title('Error de interpolacion')
    ax2.grid(True, alpha=0.3)
    
    # Marcar nodos donde error = 0
    for nodo in nodos:
        ax2.axvline(x=nodo, color='r', linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('interpolacion.png')
    print("\nGrafico guardado: interpolacion.png")

# Programa principal
if __name__ == "__main__":
    print("\nPROBLEMA 1: INTERPOLACION DE LAGRANGE")
    print("="*50)
    print("Nodos: x0 = 1, x1 = 2, x2 = 2.5")
    print("Orden del polinomio: N = 2")
    print("\n")
    
    verificar_propiedades()
    analizar_error()
    
    plt.show()