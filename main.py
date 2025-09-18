#!/usr/bin/env python3
"""
Archivo Principal - Metodos Numericos
=====================================

Este archivo sirve como punto de entrada principal para usar la biblioteca
de metodos numericos. Contiene ejemplos de uso y facilita la importacion.

Uso rapido:
    python main.py

Para importar en otros proyectos:
    from metodos_numericos import biseccion, newton_raphson, FuncionesBasicas
"""

import sys
import os

# Agregar el directorio actual al path para imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar todas las funciones principales
from metodos_numericos import (
    # Funciones matematicas
    FuncionesBasicas, FuncionesPuntoFijo, calcular_error,
    
    # Metodos de raices
    biseccion, newton_raphson, regula_falsi, punto_fijo, secante,
    
    # Sistemas lineales
    eliminacion_gaussiana, jacobi, gauss_seidel, relajacion,
    
    # Interpolacion
    lagrange, sistema_ecuaciones, spline_cubica, cuadrados_minimos,
    
    # Utilidades
    graficar_funcion, analizar_convergencia, comparar_metodos
)


def demo_localizacion_raices():
    """Demostracion de metodos de localizacion de raices"""
    print("=" * 60)
    print("DEMOSTRACION: LOCALIZACION DE RAICES")
    print("=" * 60)
    
    # Usar una funcion predefinida
    f = FuncionesBasicas.f2  # x^3 - 2x - 5
    df_dx = FuncionesBasicas.df2_dx  # 3x^2 - 2
    g = FuncionesPuntoFijo.g2  # (2x + 5)^(1/3)
    
    print("Funcion: f(x) = x³ - 2x - 5")
    print("Derivada: f'(x) = 3x² - 2")
    print("g(x) para punto fijo: g(x) = ∛(2x + 5)")
    
    # Metodo de biseccion
print()
    print("METODO DE BISECCION")
    print("="*40)
    raiz_bis, error_bis, hist_bis = biseccion(f, 2, 3, tolerancia=1e-6)
    
    # Metodo de Newton-Raphson
print()
    print("METODO DE NEWTON-RAPHSON")
    print("="*40)
    raiz_nr, error_nr, hist_nr = newton_raphson(f, df_dx, 2.5, tolerancia=1e-6)
    
    # Metodo de punto fijo
print()
    print("METODO DE PUNTO FIJO")
    print("="*40)
    raiz_pf, error_pf, hist_pf = punto_fijo(g, 2.0, tolerancia=1e-6)
    
    # Comparar resultados
    resultados = []
    if raiz_bis:
        resultados.append({
            'metodo': 'Biseccion',
            'raiz': raiz_bis,
            'error_final': error_bis,
            'iteraciones': len(hist_bis),
            'convergio': True
        })
    
    if raiz_nr:
        resultados.append({
            'metodo': 'Newton-Raphson',
            'raiz': raiz_nr,
            'error_final': error_nr,
            'iteraciones': len(hist_nr),
            'convergio': True
        })
    
    if raiz_pf:
        resultados.append({
            'metodo': 'Punto Fijo',
            'raiz': raiz_pf,
            'error_final': error_pf,
            'iteraciones': len(hist_pf),
            'convergio': True
        })
    
print()
    print("COMPARACION DE METODOS")
    print("="*60)
    
    if resultados:
        print(f"{'Metodo':<15} {'Raiz':<12} {'Error Final':<15} {'Iteraciones':<12}")
        print("-" * 60)
        for r in resultados:
            print(f"{r['metodo']:<15} {r['raiz']:<12.6f} {r['error_final']:<15.2e} {r['iteraciones']:<12}")


def demo_sistemas_lineales():
    """Demostracion de metodos para sistemas lineales"""
    print("" + "=" * 60)
    print("DEMOSTRACION: SISTEMAS DE ECUACIONES LINEALES")
    print("=" * 60)
    
    # Sistema de prueba: 
    # 3x + 2y - z = 1
    # 2x + 6y + z = 0
    # x + y + 7z = 4
    
    A = [
        [3.0, 2.0, -1.0],
        [2.0, 6.0, 1.0],
        [1.0, 1.0, 7.0]
    ]
    b = [1.0, 0.0, 4.0]
    
    print("Sistema de ecuaciones:")
    print("3x + 2y - z = 1")
    print("2x + 6y + z = 0")
    print("x + y + 7z = 4")
    
    # Eliminacion Gaussiana
print()
    print("ELIMINACION GAUSSIANA")
    print("="*40)
    solucion_gauss, mensaje = eliminacion_gaussiana(A, b)
    
    # Metodo de Jacobi
print()
    print("METODO DE JACOBI")
    print("="*40)
    solucion_jacobi, iter_jacobi, hist_jacobi = jacobi(A, b, tolerancia=1e-6, max_iter=50)
    
    # Metodo de Gauss-Seidel
print()
    print("METODO DE GAUSS-SEIDEL")
    print("="*40)
    solucion_gs, iter_gs, hist_gs = gauss_seidel(A, b, tolerancia=1e-6, max_iter=50)


def demo_interpolacion():
    """Demostracion de metodos de interpolacion"""
    print("" + "=" * 60)
    print("DEMOSTRACION: INTERPOLACION")
    print("=" * 60)
    
    # Puntos de prueba
    puntos_x = [0.0, 1.0, 2.0, 3.0]
    puntos_y = [1.0, 2.0, 5.0, 10.0]
    x_interpolar = 1.5
    
    print(f"Puntos conocidos: {list(zip(puntos_x, puntos_y))}")
    print(f"Interpolando en x = {x_interpolar}")
    
    # Interpolacion de Lagrange
print()
    print("INTERPOLACION DE LAGRANGE")
    print("="*40)
    resultado_lagrange = lagrange(puntos_x, puntos_y, x_interpolar)
    
    # Interpolacion por sistema de ecuaciones
print()
    print("INTERPOLACION POR SISTEMA")
    print("="*40)
    coeficientes, polinomio = sistema_ecuaciones(puntos_x, puntos_y)
    resultado_sistema = polinomio(x_interpolar)
    print(f"Evaluando en x = {x_interpolar}: P({x_interpolar}) = {resultado_sistema:.6f}")
    
    # Regresion por cuadrados minimos
print()
    print("REGRESION CUADRADOS MINIMOS")
    print("="*40)
    coef_regresion, poly_regresion, r2 = cuadrados_minimos(puntos_x, puntos_y, grado=2)
    resultado_regresion = poly_regresion(x_interpolar)
    print(f"Evaluando en x = {x_interpolar}: P({x_interpolar}) = {resultado_regresion:.6f}")


def menu_interactivo():
    """Menu interactivo para probar diferentes metodos"""
    while True:
        print("" + "=" * 60)
        print("MENU INTERACTIVO - METODOS NUMERICOS")
        print("=" * 60)
        print("1. Demostracion de Localizacion de Raices")
        print("2. Demostracion de Sistemas Lineales")
        print("3. Demostracion de Interpolacion")
        print("4. Ejecutar todas las demostraciones")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opcion (1-5): ").strip()
        
        if opcion == '1':
            demo_localizacion_raices()
        elif opcion == '2':
            demo_sistemas_lineales()
        elif opcion == '3':
            demo_interpolacion()
        elif opcion == '4':
            demo_localizacion_raices()
            demo_sistemas_lineales()
            demo_interpolacion()
        elif opcion == '5':
            break
        else:
            print("Opcion no valida. Por favor, seleccione 1-5.")

        input("\nPresione Enter para continuar...")


def mostrar_ayuda():
    """Muestra informacion de ayuda sobre el uso de la biblioteca"""
    print("""
========================================
AYUDA - BIBLIOTECA METODOS NUMERICOS
========================================

Esta biblioteca contiene implementaciones de metodos numericos organizados en modulos:

MODULOS DISPONIBLES:
-------------------

1. funciones: Funciones matematicas y utilidades
   - FuncionesBasicas: Funciones predefinidas comunes
   - FuncionesPuntoFijo: Funciones g(x) para punto fijo
   - calcular_error: Calculo de errores absolutos y porcentuales

2. localizacion_raices: Metodos para encontrar raices
   - biseccion(f, a, b, tolerancia, tipo_error, max_iter)
   - newton_raphson(f, df_dx, x0, tolerancia, tipo_error, max_iter)
   - regula_falsi(f, a, b, tolerancia, tipo_error, max_iter)
   - punto_fijo(g, x0, tolerancia, tipo_error, max_iter)
   - secante(f, x0, x1, tolerancia, tipo_error, max_iter)

3. sistemas_lineales: Metodos para sistemas de ecuaciones
   - eliminacion_gaussiana(A, b, mostrar_pasos)
   - jacobi(A, b, x0, tolerancia, max_iter)
   - gauss_seidel(A, b, x0, tolerancia, max_iter)
   - relajacion(A, b, omega, x0, tolerancia, max_iter)

4. interpolacion: Metodos de interpolacion y regresion
   - lagrange(puntos_x, puntos_y, x_interpolar)
   - sistema_ecuaciones(puntos_x, puntos_y)
   - spline_cubica(puntos_x, puntos_y, condicion_frontera)
   - cuadrados_minimos(puntos_x, puntos_y, grado)

5. utilidades: Funciones auxiliares
   - graficar_funcion(f, intervalo, num_puntos)
   - analizar_convergencia(historial, metodo, tolerancia)
   - comparar_metodos(resultados_metodos, criterio)

EJEMPLO DE USO:
--------------

from metodos_numericos import biseccion, FuncionesBasicas

# Usar funcion predefinida
f = FuncionesBasicas.f2  # x^3 - 2x - 5

# Encontrar raiz
raiz, error, historial = biseccion(f, 2, 3, tolerancia=1e-6)

print(f"Raiz encontrada: {raiz}")
print(f"Error final: {error}")
print(f"Iteraciones: {len(historial)}")

Para mas informacion, consulte la documentacion de cada funcion.
""")


if __name__ == "__main__":
    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help', 'help']:
            mostrar_ayuda()
        elif sys.argv[1] == 'demo':
            demo_localizacion_raices()
            demo_sistemas_lineales()
            demo_interpolacion()
        else:
            print(f"Argumento no reconocido: {sys.argv[1]}")
            print("Uso: python main.py [demo|help]")
    else:
        # Menu interactivo por defecto
        menu_interactivo()