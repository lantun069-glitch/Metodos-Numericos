import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from metodos_numericos.interpolacion import sistema_ecuaciones
from metodos_numericos.localizacion_raices import biseccion
from metodos_numericos.funciones import verificar_cambio_signo

def main():
    print("Ejercicio 01 - Parcial 1")
    print("-" * 30)

    # Datos del problema
    puntos_x = [2.0, 3.0, 4.0, 5.0]
    puntos_y = [1.0, 0.7, -0.2, -1.0]

    # a) Interpolacion
    print()
    print("-" * 30)
    coeficientes, polinomio = sistema_ecuaciones(puntos_x, puntos_y)

    # b) Encontrar raiz por biseccion
    print()
    print("-" * 30)

    # Buscar intervalo para la raiz mas pequena
    print("Buscando intervalos con cambio de signo:")

    intervalos_con_raiz = []
    paso = 0.1
    x_min = 0.0  # Buscar desde x=0 para asegurar encontrar raices negativas
    x_max = 6.0  # Buscar hasta mas alla del ultimo punto dado

    a = x_min
    while a < x_max - paso:
        b = a + paso
        if verificar_cambio_signo(polinomio, a, b):
            intervalos_con_raiz.append((a, b))
            print(f"Cambio de signo en [{a:.1f}, {b:.1f}]")
        a = b

    if not intervalos_con_raiz:
        print("No se encontraron intervalos con cambio de signo en el rango explorado.")
        return

    # Ordenar intervalos para asegurar que tomamos la raiz mas pequena
    intervalos_con_raiz.sort()

    # Usar el primer intervalo (raiz mas pequena)
    a, b = intervalos_con_raiz[0]
    print(f"Intervalo seleccionado para la raiz mas pequena: [{a:.1f}, {b:.1f}]")

    # Aplicar biseccion con error porcentual de 0.1%
    resultado = biseccion(polinomio, a, b, tolerancia=0.1, tipo_error='porcentual')
    raiz, f_raiz, error = resultado

    # Resultados
    print()
    print(f"Intervalo empleado: [{a:.1f}, {b:.1f}]")
    print(f"Raiz encontrada: {raiz}")
    print(f"Error porcentual: {error}%")

if __name__ == "__main__":
    main()