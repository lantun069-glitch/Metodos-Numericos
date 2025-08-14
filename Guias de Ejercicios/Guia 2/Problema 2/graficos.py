import numpy as np
import matplotlib.pyplot as plt

def graficar_funcion(g_func, nombre, x_min, x_max, punto_fijo=None):
    x = np.linspace(x_min, x_max, 500)
    y = []
    
    for xi in x:
        try:
            yi = g_func(xi)
            if abs(yi) < 10:
                y.append(yi)
            else:
                y.append(np.nan)
        except:
            y.append(np.nan)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'b-', label=f'g(x) = {nombre}')
    plt.plot(x, x, 'r--', label='y = x')
    
    if punto_fijo is not None:
        plt.plot(punto_fijo, punto_fijo, 'ro', markersize=8, label=f'Punto fijo: {punto_fijo:.6f}')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'g(x) = {nombre}')
    plt.legend()
    plt.grid(True)
    
    filename = f'grafico_{nombre.replace("^", "").replace("(", "").replace(")", "").replace(" ", "_")}.png'
    plt.savefig(filename)
    plt.close()
    return filename