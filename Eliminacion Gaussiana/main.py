from typing import List
from gauss_elim import eliminacion_gaussiana, MatrizSingularError
from utils import mostrar_matriz, mostrar_vector

def main() -> None:
    # Sistema de ejemplo (reemplazar por sistema):
    #   0.0001 x1 +   x2 +  3 x3 = 1
    #   2     x1 +  2 x2 -  3 x3 = 3
    #  -5     x1 +  0 x2 +  1 x3 = 5
    A: List[List[float]] = [
        [0.0001, 1.0, 3.0],
        [2.0,    2.0, -3.0],
        [-5.0,   0.0, 1.0],
    ]
    b: List[float] = [1.0, 3.0, 5.0]

    print("A:\n" + mostrar_matriz(A))
    print("b: " + mostrar_vector(b))

    try:
        x, U, c = eliminacion_gaussiana(A, b, tol=1e-12, mostrar_pasos=True)
    except MatrizSingularError as e:
        print("Error:", e)
        return

    print("\nU:\n" + mostrar_matriz(U))
    print("c: " + mostrar_vector(c))
    print("\nSolucion x: " + mostrar_vector(x))

if __name__ == "__main__":
    main()
