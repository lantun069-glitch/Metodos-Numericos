from typing import List
from gauss_elim import eliminacion_gaussiana, MatrizSingularError
from utils import mostrar_matriz, mostrar_vector

def main() -> None:
    # Sistema de ecuaciones del Problema 2:
    # a1 + 2a2 + a3 + 4a4 = 13
    # 2a2 + 4a3 + 3a4 = 28  
    # 4a1 + 2a2 + 2a3 + a4 = 20
    # -3a1 + a2 + 3a3 + 2a4 = 6
    
    A: List[List[float]] = [
        [1.0, 2.0, 1.0, 4.0],   # a1 + 2a2 + a3 + 4a4 = 13
        [0.0, 2.0, 4.0, 3.0],   # 2a2 + 4a3 + 3a4 = 28
        [4.0, 2.0, 2.0, 1.0],   # 4a1 + 2a2 + 2a3 + a4 = 20
        [-3.0, 1.0, 3.0, 2.0]   # -3a1 + a2 + 3a3 + 2a4 = 6
    ]
    
    b: List[float] = [13.0, 28.0, 20.0, 6.0]
    
    print("Sistema de ecuaciones:")
    print("a1 + 2a2 + a3 + 4a4 = 13")
    print("2a2 + 4a3 + 3a4 = 28")
    print("4a1 + 2a2 + 2a3 + a4 = 20")
    print("-3a1 + a2 + 3a3 + 2a4 = 6")
    print()
    
    print("Matriz A:")
    print(mostrar_matriz(A))
    print()
    print("Vector b:", mostrar_vector(b))
    print()
    
    try:
        x, U, c = eliminacion_gaussiana(A, b, tol=1e-12, mostrar_pasos=False)
        
        print("=== RESULTADOS ===")
        print("Solucion encontrada:")
        print(f"a1 = {x[0]:.3f}")
        print(f"a2 = {x[1]:.3f}")
        print(f"a3 = {x[2]:.3f}")
        print(f"a4 = {x[3]:.3f}")
        print()
        
        # Calcular determinante
        from utils import producto_diagonal
        det_A = producto_diagonal(U)
        print(f"det(A) = {det_A:.0f}")
        
        # Verificacion de la solucion
        print("\n=== VERIFICACION ===")
        for i in range(len(A)):
            suma = sum(A[i][j] * x[j] for j in range(len(x)))
            print(f"Ecuacion {i+1}: {suma:.6f} ≈ {b[i]:.6f}")
            
    except MatrizSingularError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()