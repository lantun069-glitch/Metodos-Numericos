#!/usr/bin/env python3
"""
Tests basicos para verificar la instalacion
==========================================
"""

import sys
import os

# Agregar path si es necesario
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Prueba que todos los modulos se puedan importar"""
    try:
        from metodos_numericos import (
            biseccion, newton_raphson, regula_falsi, punto_fijo,
            eliminacion_gaussiana, jacobi, gauss_seidel,
            lagrange, cuadrados_minimos,
            FuncionesBasicas
        )
        print("✓ Todos los imports funcionan correctamente")
        return True
    except ImportError as e:
        print(f"✗ Error en imports: {e}")
        return False

def test_biseccion():
    """Test basico del metodo de biseccion"""
    try:
        from metodos_numericos import biseccion, FuncionesBasicas
        
        f = FuncionesBasicas.f2  # x^3 - 2x - 5
        raiz, error, hist = biseccion(f, 2, 3, tolerancia=1e-6, mostrar_iteraciones=False)
        
        if raiz and abs(f(raiz)) < 1e-5:
            print("✓ Test biseccion: PASO")
            return True
        else:
            print("✗ Test biseccion: FALLO")
            return False
    except Exception as e:
        print(f"✗ Test biseccion: ERROR - {e}")
        return False

def test_sistema_lineal():
    """Test basico de sistema lineal"""
    try:
        from metodos_numericos import eliminacion_gaussiana
        
        A = [[2, 1], [1, 3]]
        b = [3, 4]
        
        solucion, mensaje = eliminacion_gaussiana(A, b, mostrar_pasos=False)
        
        if solucion and len(solucion) == 2:
            print("✓ Test sistema lineal: PASO")
            return True
        else:
            print("✗ Test sistema lineal: FALLO")
            return False
    except Exception as e:
        print(f"✗ Test sistema lineal: ERROR - {e}")
        return False

def ejecutar_todos_tests():
    """Ejecuta todos los tests"""
    print("=" * 50)
    print("EJECUTANDO TESTS DE VERIFICACION")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_biseccion,
        test_sistema_lineal
    ]
    
    resultados = []
    for test in tests:
        resultado = test()
        resultados.append(resultado)
    
    total = len(resultados)
    pasaron = sum(resultados)
    
print()
    print(f"RESULTADOS: {pasaron}/{total} tests pasaron")
    print("=" * 50)
    
    if pasaron == total:
        print("🎉 ¡Todos los tests pasaron! La instalacion esta correcta.")
    else:
        print("⚠️  Algunos tests fallaron. Revisar la instalacion.")
    
    return pasaron == total

if __name__ == "__main__":
    ejecutar_todos_tests()
