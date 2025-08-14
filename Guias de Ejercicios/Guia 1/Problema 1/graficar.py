import numpy as np
import matplotlib.pyplot as plt
from funciones import f

def graficar_funcion():
    """Grafica la funcion f(x)"""
    
    x = np.linspace(-1, 2, 1000)
    y = [f(xi) for xi in x]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='f(x) = -2 + 7x - 5x² + 6x³')
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.5, label='y = 0')
    plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)
    
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Grafico de f(x) = -2 + 7x - 5x² + 6x³')
    plt.legend()
    plt.xlim(-0.5, 2)
    plt.ylim(-3, 8)
    
    plt.savefig('grafico_funcion.png', dpi=300, bbox_inches='tight')
    plt.close()