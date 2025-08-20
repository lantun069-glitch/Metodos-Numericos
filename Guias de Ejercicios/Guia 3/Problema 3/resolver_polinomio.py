# Problema 3: Hallar el polinomio cubico y = A + Bx + Cx^2 + Dx^3
# que pasa por los puntos (0,0), (1,1), (2,3), (3,4)

def resolver_sistema_polinomio():
    """
    Resuelve el sistema para encontrar coeficientes del polinomio cubico
    que pasa por los puntos dados.
    """
    # Puntos dados: (x, y)
    puntos = [(0, 0), (1, 1), (2, 3), (3, 4)]
    
    # Construir matriz del sistema
    # Para cada punto (xi, yi): yi = A + B*xi + C*xi^2 + D*xi^3
    n = len(puntos)
    matriz = []
    vector_b = []
    
    for x, y in puntos:
        fila = [1, x, x**2, x**3]  # Coeficientes de [A, B, C, D]
        matriz.append(fila)
        vector_b.append(y)
    
    print("Sistema de ecuaciones para el polinomio cubico:")
    print("Matriz de coeficientes:")
    for i, fila in enumerate(matriz):
        print(f"  {fila} -> y = {vector_b[i]}")
    
    # Resolver usando eliminacion gaussiana con pivoteo parcial
    solucion = eliminacion_gaussiana(matriz, vector_b)
    
    return solucion

def eliminacion_gaussiana(A, b):
    """
    Resuelve Ax = b usando eliminacion gaussiana con pivoteo parcial.
    """
    n = len(A)
    # Crear copias para no modificar originales
    matriz = [fila[:] for fila in A]
    vector = b[:]
    
    # Eliminacion hacia adelante con pivoteo parcial
    for i in range(n-1):
        # Buscar pivote maximo
        max_val = abs(matriz[i][i])
        max_row = i
        for k in range(i+1, n):
            if abs(matriz[k][i]) > max_val:
                max_val = abs(matriz[k][i])
                max_row = k
        
        # Intercambiar filas si es necesario
        if max_row != i:
            matriz[i], matriz[max_row] = matriz[max_row], matriz[i]
            vector[i], vector[max_row] = vector[max_row], vector[i]
        
        # Hacer ceros debajo del pivote
        for j in range(i+1, n):
            if matriz[i][i] != 0:
                factor = matriz[j][i] / matriz[i][i]
                for k in range(i, n):
                    matriz[j][k] -= factor * matriz[i][k]
                vector[j] -= factor * vector[i]
    
    # Sustitucion hacia atras
    x = [0] * n
    for i in range(n-1, -1, -1):
        suma = vector[i]
        for j in range(i+1, n):
            suma -= matriz[i][j] * x[j]
        x[i] = suma / matriz[i][i]
    
    return x

def verificar_polinomio(coeficientes, puntos):
    """
    Verifica que el polinomio pase por los puntos dados.
    """
    A, B, C, D = coeficientes
    print("\nVerificacion del polinomio:")
    for x, y_esperado in puntos:
        y_calculado = A + B*x + C*x**2 + D*x**3
        print(f"  Punto ({x}, {y_esperado}): y_calculado = {y_calculado:.6f}")

def main():
    print("=" * 60)
    print("PROBLEMA 3: Polinomio Cubico por 4 Puntos")
    print("=" * 60)
    
    # Resolver el sistema
    coeficientes = resolver_sistema_polinomio()
    
    # Mostrar resultados
    A, B, C, D = coeficientes
    print("\n" + "=" * 60)
    print("SOLUCION:")
    print("=" * 60)
    print(f"Coeficientes del polinomio:")
    print(f"  A = {A:.6f}")
    print(f"  B = {B:.6f}")
    print(f"  C = {C:.6f}")
    print(f"  D = {D:.6f}")
    
    print(f"\nPolinomio cubico:")
    # Formatear polinomio de forma legible
    terminos = []
    if abs(A) > 1e-10:
        terminos.append(f"{A:.6f}")
    if abs(B) > 1e-10:
        signo = "+" if B > 0 and terminos else ""
        terminos.append(f"{signo}{B:.6f}x")
    if abs(C) > 1e-10:
        signo = "+" if C > 0 and terminos else ""
        terminos.append(f"{signo}{C:.6f}x^2")
    if abs(D) > 1e-10:
        signo = "+" if D > 0 and terminos else ""
        terminos.append(f"{signo}{D:.6f}x^3")
    
    print(f"  y = {''.join(terminos)}")
    
    # Verificar la solucion
    puntos = [(0, 0), (1, 1), (2, 3), (3, 4)]
    verificar_polinomio(coeficientes, puntos)

if __name__ == "__main__":
    main()