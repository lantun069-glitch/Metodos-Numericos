"""
Parcial 1 - Ejercicio 01
=========================
Sistemas de Ecuaciones Lineales
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from metodos_numericos import *

def main():
    print("Ejercicio 02 - Parcial 2")
    print("-" * 30)
    
    # a) Encontrar el polinomio que interpola los valores de la tabla
    puntos_x = [2.0, 3.0, 4.0, 5.0]
    puntos_y = [1.0, 0.7, -0.2, -1.0]

    print("a) Polinomio interpolador")
    coeficientes, polinomio = sistema_ecuaciones(puntos_x, puntos_y)

    print("Coeficientes del polinomio interpolador:")
    for i, coef in enumerate(coeficientes):
        print(f"  a{i} = {coef:.6f}")

    # Imprimir la expresion del polinomio
    terminos = []
    for i, coef in enumerate(coeficientes):
        if i == 0:
            terminos.append(f"{coef:.6f}")
        elif i == 1:
            terminos.append(f"{coef:.6f}x")
        else:
            terminos.append(f"{coef:.6f}x^{i}")
    print(f"P(x) = {' + '.join(terminos)}")

    # b) Encontrar la raiz mas pequena utilizando biseccion
    print()

    # Evaluamos el polinomio en muchos puntos para detectar cambios de signo
    x_min = min(puntos_x)  # 2.0
    x_max = max(puntos_x)  # 5.0

    # Crear una malla fina de puntos
    paso = 0.01  # Paso fino para mayor precision
    puntos_malla = [x_min + i * paso for i in range(int((x_max - x_min) / paso) + 1)]
    valores_polinomio = [polinomio(x) for x in puntos_malla]

    # Buscar el primer cambio de signo (raiz mas a la izquierda)
    intervalo_con_raiz = None
    for i in range(len(puntos_malla) - 1):
        if valores_polinomio[i] * valores_polinomio[i + 1] <= 0:
            intervalo_con_raiz = (puntos_malla[i], puntos_malla[i + 1])
            break  # Tomamos el primer intervalo con cambio de signo

    if not intervalo_con_raiz:
        print("No se encontraron intervalos con cambio de signo")
        return

    a, b = intervalo_con_raiz
    print(f"Intervalo inicial que contiene la raiz mas pequena: [{a}, {b}]")

    # Aplicar metodo de biseccion con error porcentual de 0.1%
    resultado = biseccion(polinomio, a, b, tolerancia=0.001, tipo_error='porcentual')
    raiz, f_raiz, error = resultado

    print()
    print(f"Intervalo empleado: [{a}, {b}]")
    print(f"Valor obtenido de la raiz: {raiz}")
    print(f"Error porcentual obtenido: {error:.4f}%")
    print(f"Valor de la funcion en la raiz: {polinomio(raiz):.10f}")
    
    
if __name__ == "__main__":
    main()
