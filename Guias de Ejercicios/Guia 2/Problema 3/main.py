from algoritmos_raices import raiz_cuadrada_formula, raiz_cubica_formula, newton_raphson_raiz
import math

def main():
    print("Algoritmo de la raiz cuadrada y cubica")
    print("="*50)
    
    # Caso cuadratico: A = 2
    A = 2
    p0 = 1.0
    print(f"\nCASO CUADRATICO: A = {A}")
    print(f"Valor inicial: p0 = {p0}")
    
    resultado_formula = raiz_cuadrada_formula(A, p0)
    print()
    resultado_newton = newton_raphson_raiz(A, 2, p0)
    
    print(f"\nResultados:")
    print(f"Formula: {resultado_formula:.8f}")
    print(f"Newton-Raphson: {resultado_newton:.8f}")
    print(f"math.sqrt({A}): {math.sqrt(A):.8f}")
    
    # Caso cubico: A = 8
    A = 8
    p0 = 2.0
    print(f"\n\nCASO CUBICO: A = {A}")
    print(f"Valor inicial: p0 = {p0}")
    
    resultado_formula = raiz_cubica_formula(A, p0)
    print()
    resultado_newton = newton_raphson_raiz(A, 3, p0)
    
    print(f"\nResultados:")
    print(f"Formula: {resultado_formula:.8f}")
    print(f"Newton-Raphson: {resultado_newton:.8f}")
    print(f"Valor exacto: {8**(1/3):.8f}")

if __name__ == "__main__":
    main()