import numpy as np
import matplotlib.pyplot as plt

def graficar_funcion(funcion_str, x_min=-10, x_max=10, num_puntos=1000, guardar=False, nombre_archivo='grafica.png'):
    """
    Grafica una función matemática proporcionada como string, resalta las raíces y guarda si se desea.

    Parámetros:
    - funcion_str: str, función matemática en términos de 'x' (ej. 'np.sin(x)', 'x**2', etc.)
    - x_min: float, mínimo del eje x
    - x_max: float, máximo del eje x
    - num_puntos: int, cantidad de puntos a generar
    - guardar: bool, si True, guarda la imagen como archivo PNG
    - nombre_archivo: str, nombre del archivo a guardar (debe terminar en .png)
    """
    try:
        x = np.linspace(x_min, x_max, num_puntos)
        y = eval(funcion_str)

        plt.figure(figsize=(10, 5))
        plt.plot(x, y, label=f"f(x) = {funcion_str}", color='blue')
        plt.title("Gráfica de la función")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)

        # Ejes
        plt.axhline(0, color='red', linewidth=1.0, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5)

        # === DETECCIÓN DE RAÍCES ===
        raices_x = []
        for i in range(len(x) - 1):
            if y[i] * y[i + 1] < 0:  # Cambio de signo ⇒ raíz
                x0, x1 = x[i], x[i + 1]
                y0, y1 = y[i], y[i + 1]
                raiz = x0 - y0 * (x1 - x0) / (y1 - y0)  # Interpolación lineal
                raices_x.append(raiz)

        # Mostrar raíces
        if raices_x:
            plt.scatter(raices_x, [0] * len(raices_x), color='red', zorder=5, label='Raíces')
            print("Raíces encontradas:")
            for r in raices_x:
                print(f"x ≈ {r:.6f}")
        else:
            print("No se encontraron raíces en el intervalo dado.")

        plt.legend()
        plt.tight_layout()

        if guardar:
            plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
            print(f"Gráfica guardada como '{nombre_archivo}'")

        plt.show()

    except Exception as e:
        print(f"Error al graficar la función: {e}")

# === Ejemplo de uso ===
graficar_funcion('2*x**2 - 8', x_min=-2*np.pi, x_max=2*np.pi, guardar=True, nombre_archivo='grafico_raices.png')
