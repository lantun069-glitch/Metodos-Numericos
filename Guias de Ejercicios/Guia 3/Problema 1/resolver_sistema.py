from typing import List
from gauss_elim import eliminacion_gaussiana, MatrizSingularError
from utils import mostrar_matriz, mostrar_vector, producto_diagonal

def main():
    print("=" * 60)
    print("RESOLUCION DE SISTEMA DE ECUACIONES LINEALES")
    print("=" * 60)
    
    # Sistema de ecuaciones dado:
    # 4x1 - x2 + 2x3 + 3x4 = 20
    # -2x2 + 7x3 - 4x4 = -7
    # 6x3 + 5x4 = 4
    # 3x4 = 6
    
    A: List[List[float]] = [
        [4.0, -1.0, 2.0, 3.0],
        [0.0, -2.0, 7.0, -4.0],
        [0.0, 0.0, 6.0, 5.0],
        [0.0, 0.0, 0.0, 3.0]
    ]
    
    b: List[float] = [20.0, -7.0, 4.0, 6.0]
    
    print("Matriz A:")
    print(mostrar_matriz(A))
    print("\nVector b:")
    print(mostrar_vector(b))
    
    try:
        # Resolver el sistema usando eliminacion gaussiana
        x, U, c = eliminacion_gaussiana(A, b, tol=1e-12, mostrar_pasos=False)
        
        print("\n" + "=" * 40)
        print("RESULTADOS")
        print("=" * 40)
        
        # Mostrar la solucion
        print("Solucion del sistema:")
        for i, valor in enumerate(x):
            print(f"x{i+1} = {valor:.0f}")
        
        # Calcular el determinante
        # Como A ya es triangular superior, det(A) = producto de la diagonal
        det_A = producto_diagonal(A)
        print(f"\nDeterminante de A: det(A) = {det_A:.0f}")
        
        # Verificacion de la solucion
        print("\n" + "-" * 40)
        print("VERIFICACION:")
        print("-" * 40)
        
        # Calcular Ax para verificar que Ax = b
        n = len(A)
        Ax = [0.0] * n
        for i in range(n):
            for j in range(n):
                Ax[i] += A[i][j] * x[j]
        
        print("Ax =", mostrar_vector(Ax))
        print("b  =", mostrar_vector(b))
        
        # Verificar si Ax ≈ b
        error_max = max(abs(Ax[i] - b[i]) for i in range(n))
        print(f"Error maximo |Ax - b|: {error_max:.2e}")
        
        if error_max < 1e-10:
            print("✓ Verificacion exitosa: Ax = b")
        else:
            print("✗ Error en la verificacion")
            
    except MatrizSingularError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()