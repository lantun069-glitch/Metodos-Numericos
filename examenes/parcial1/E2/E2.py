import numpy as np
from copy import deepcopy
import sys
import os

def mostrar_matriz(A, nombre="Matriz"):
    """Muestra una matriz de forma legible"""
    print(f"\n{nombre}:")
    for fila in A:
        print("  ".join(f"{x:8.4f}" for x in fila))

def mostrar_vector(v, nombre="Vector"):
    """Muestra un vector de forma legible"""
    print(f"\n{nombre}:")
    print("  ".join(f"{x:8.4f}" for x in v))

def eliminacion_gaussiana(A, b, mostrar_pasos=False):
    """
    Implementa el método de eliminación gaussiana con pivoteo parcial.
    
    Args:
        A: Matriz de coeficientes
        b: Vector de términos independientes
        mostrar_pasos: Si True, muestra los pasos intermedios
        
    Returns:
        Solución del sistema
    """
    n = len(A)
    
    # Copiar matrices para no modificar las originales
    A_temp = deepcopy(A)
    b_temp = deepcopy(b)
    
    # Comprobar si se utilizó pivoteo
    se_uso_pivoteo = False
    
    # Eliminación hacia adelante
    for k in range(n):
        # Pivoteo parcial
        max_fila = k
        for i in range(k+1, n):
            if abs(A_temp[i][k]) > abs(A_temp[max_fila][k]):
                max_fila = i
                se_uso_pivoteo = True
        
        # Intercambiar filas si es necesario
        if max_fila != k:
            A_temp[k], A_temp[max_fila] = A_temp[max_fila], A_temp[k]
            b_temp[k], b_temp[max_fila] = b_temp[max_fila], b_temp[k]
            if mostrar_pasos:
                print(f"\nIntercambio de filas {k+1} y {max_fila+1} para pivoteo")
                mostrar_matriz(A_temp, "Matriz después de intercambio")
        
        # Eliminación
        for i in range(k+1, n):
            if abs(A_temp[k][k]) < 1e-10:  # Evitar división por cero
                print("Error: Pivote cercano a cero, posible matriz singular")
                continue
                
            factor = A_temp[i][k] / A_temp[k][k]
            for j in range(k, n):
                A_temp[i][j] -= factor * A_temp[k][j]
            b_temp[i] -= factor * b_temp[k]
        
        if mostrar_pasos:
            mostrar_matriz(A_temp, f"Matriz después de eliminación paso {k+1}")
            mostrar_vector(b_temp, "Vector b actualizado")
    
    # Sustitución hacia atrás
    x = [0] * n
    for i in range(n-1, -1, -1):
        suma = 0
        for j in range(i+1, n):
            suma += A_temp[i][j] * x[j]
        if abs(A_temp[i][i]) < 1e-10:
            print("Error: Diagonal cercana a cero en sustitución hacia atrás")
            return None
        x[i] = (b_temp[i] - suma) / A_temp[i][i]
    
    return x, se_uso_pivoteo

def es_diagonal_dominante(A):
    """
    Verifica si la matriz A es estrictamente diagonal dominante.
    Una matriz es estrictamente diagonal dominante si en cada fila,
    el valor absoluto del elemento diagonal es mayor que la suma de 
    los valores absolutos de los demás elementos de la fila.
    """
    n = len(A)
    for i in range(n):
        diagonal = abs(A[i][i])
        suma_resto = sum(abs(A[i][j]) for j in range(n) if j != i)
        if diagonal <= suma_resto:
            return False, i  # No es diagonal dominante, devuelve la fila problemática
    return True, -1  # Es diagonal dominante

def verificar_gauss_seidel(A):
    """
    Verifica si el método de Gauss-Seidel probablemente convergerá
    basado en criterios de dominancia diagonal.
    """
    es_dominante, fila_problema = es_diagonal_dominante(A)
    
    # Verificar condiciones para convergencia de Gauss-Seidel
    if es_dominante:
        return True, "La matriz es estrictamente diagonal dominante, Gauss-Seidel convergería."
    else:
        mensaje = f"La matriz NO es estrictamente diagonal dominante (ver fila {fila_problema+1}). "
        mensaje += "La convergencia de Gauss-Seidel no está garantizada."
        return False, mensaje

def calcular_error_absoluto(x_nuevo, x_viejo):
    """Calcula el error absoluto máximo entre dos vectores"""
    return max(abs(x_nuevo[i] - x_viejo[i]) for i in range(len(x_nuevo)))

def gauss_seidel(A, b, x0=None, tolerancia=1e-5, max_iter=100):
    """
    Implementa el método de Gauss-Seidel para sistemas lineales.
    
    Args:
        A: Matriz de coeficientes
        b: Vector de términos independientes
        x0: Vector inicial (por defecto, vector de ceros)
        tolerancia: Criterio de parada para el error absoluto
        max_iter: Número máximo de iteraciones
        
    Returns:
        Solución aproximada, número de iteraciones, error final
    """
    n = len(A)
    if x0 is None:
        x0 = [1.0] * n  # Vector inicial con unos
    
    x = x0[:]  # Copia del vector inicial
    iteraciones = 0
    error = float('inf')
    
    for iteracion in range(max_iter):
        x_anterior = x[:]
        
        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    suma += A[i][j] * x[j]
            x[i] = (b[i] - suma) / A[i][i]
        
        # Calcular error
        error = calcular_error_absoluto(x, x_anterior)
        iteraciones = iteracion + 1
        
        if error < tolerancia:
            break
    
    return x, iteraciones, error

def main():

    # Definir matriz de coeficientes
    A = [
        [4, 1, 0, 0, 0, -1],
        [2, 10, -1, 0, -2, 0],
        [0, 3, 8, 0, -1, -3],
        [0, -1, 0, 4, 0, 1],
        [1, -2, 0, 0, 5, 0],
        [0, 0, 3, -2, 0, 6]
    ]
    
    # Vector de terminos independientes
    b = [0, 9, 7, 20, 22, 37]
    


    # a)
    print("\na)")
    
    solucion, se_uso_pivoteo = eliminacion_gaussiana(A, b, mostrar_pasos=False)
    
    print("solucion por eliminacion gaussiana:")
    for i, valor in enumerate(solucion):
        print(f"x{i+1} = {valor:.10f}")
    
    # b) Se puede usar gauss seide?
    print("\nb)")
    
    es_aplicable, mensaje = verificar_gauss_seidel(A)
    print(mensaje)
    
    if es_aplicable:
        print("\nPor gauss seidel:")
        solucion_gs, iteraciones, error_final = gauss_seidel(A, b, tolerancia=1e-4)
        
        print("\nSolución por Gauss-Seidel:")
        for i, valor in enumerate(solucion_gs):
            print(f"x{i+1} = {valor:.10f}")
        
        print(f"\numero de iteraciones: {iteraciones}")
        print(f"Error absoluto: {error_final:.10e}")
        
        # Calcular error 
        if solucion:
            error_estimado = max(abs(solucion_gs[i] - solucion[i]) for i in range(len(solucion)))
            print(f"Error etimado: {error_estimado:.10e}")

if __name__ == "__main__":
    main()