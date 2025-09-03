import numpy as np
from metodo_relajacion import metodo_relajacion

def main():
    print("="*70)
    print("PROBLEMA 5: METODO DE GAUSS-SEIDEL CON RELAJACION")
    print("="*70)
    
    # Definir la matriz A del sistema
    A = np.array([
        [3, -2, 1, 0, 0, 0],
        [-2, 4, -2, 1, 0, 0],
        [1, -2, 4, -2, 1, 0],
        [0, 1, -2, 4, -2, 1],
        [0, 0, 1, -2, 4, -2],
        [0, 0, 0, 1, -2, 3]
    ], dtype=float)
    
    # Definir el vector b
    b = np.array([10, -8, 10, 10, -8, 10], dtype=float)
    
    # Iteracion anterior dada x_k
    x_inicial = np.array([0, 0, 0, 0, 0, 0], dtype=float)
    # Se indica que se obtiene una interpolacion de valores entre x_k y x_k+1
    # Como no se especifica x_k, usamos vector cero como inicial
    
    print("\nMatriz A:")
    print(A)
    print("\nVector b:")
    print(b)
    print("\nVector inicial x_0:")
    print(x_inicial)
    
    # Tolerancia para convergencia
    tolerancia = 1e-6
    
    print("\n" + "-"*70)
    print("CASO 1: GAUSS-SEIDEL ESTANDAR (omega = 1.0)")
    print("-"*70)
    
    sol1, iter1, error1 = metodo_relajacion(A, b, x_inicial, omega=1.0, 
                                            tolerancia=tolerancia)
    
    if sol1 is not None:
        print(f"\nSolucion encontrada en {iter1} iteraciones")
        print(f"Error final: {error1:.6e}")
        print("Solucion x:")
        for i, xi in enumerate(sol1):
            print(f"  x{i+1} = {xi:.6f}")
    
    print("\n" + "-"*70)
    print("CASO 2: SOBRE-RELAJACION (omega = 1.1)")
    print("-"*70)
    
    sol2, iter2, error2 = metodo_relajacion(A, b, x_inicial, omega=1.1,
                                            tolerancia=tolerancia)
    
    if sol2 is not None:
        print(f"\nSolucion encontrada en {iter2} iteraciones")
        print(f"Error final: {error2:.6e}")
        print("Solucion x:")
        for i, xi in enumerate(sol2):
            print(f"  x{i+1} = {xi:.6f}")
    
    # Comparacion de resultados
    print("\n" + "="*70)
    print("COMPARACION DE RESULTADOS")
    print("="*70)
    
    print(f"Iteraciones con omega = 1.0: {iter1}")
    print(f"Iteraciones con omega = 1.1: {iter2}")
    
    if iter2 < iter1:
        mejora = ((iter1 - iter2) / iter1) * 100
        print(f"\nLa sobre-relajacion mejoro la convergencia en {mejora:.1f}%")
        print(f"Se ahorraron {iter1 - iter2} iteraciones")
    elif iter2 > iter1:
        print(f"\nLa sobre-relajacion empeoro la convergencia")
        print(f"Se necesitaron {iter2 - iter1} iteraciones adicionales")
    else:
        print("\nAmbos metodos convergieron en el mismo numero de iteraciones")
    
    # Verificacion: comprobar que Ax = b
    print("\n" + "-"*70)
    print("VERIFICACION DE LA SOLUCION (omega = 1.1)")
    print("-"*70)
    
    if sol2 is not None:
        Ax = np.dot(A, sol2)
        residuo = b - Ax
        norma_residuo = np.linalg.norm(residuo)
        
        print("Ax =", Ax)
        print("b  =", b)
        print(f"Norma del residuo ||b - Ax|| = {norma_residuo:.6e}")
        
        if norma_residuo < 1e-5:
            print("\nLa solucion es correcta (residuo muy pequeno)")
        else:
            print("\nAdvertencia: el residuo es mayor de lo esperado")

if __name__ == "__main__":
    main()