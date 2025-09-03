from typing import List, Tuple

def leer_datos(nombre_archivo: str) -> Tuple[List[float], List[float]]:
    """
    Lee los datos de interpolacion desde un archivo de texto.
    El archivo debe tener el formato:
    x0 y0
    x1 y1
    x2 y2
    ...
    """
    puntos_x = []
    puntos_y = []
    
    # Si no tiene extension, agregar .txt automaticamente
    if '.' not in nombre_archivo:
        nombre_archivo += '.txt'
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                # Ignorar lineas vacias y comentarios
                linea = linea.strip()
                if linea and not linea.startswith('#'):
                    # Separar los valores x e y
                    valores = linea.split()
                    if len(valores) >= 2:
                        x = float(valores[0])
                        y = float(valores[1])
                        puntos_x.append(x)
                        puntos_y.append(y)
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{nombre_archivo}'")
        print("Asegurate de que el archivo existe en el directorio actual")
        print("Formato esperado: cada linea debe contener 'x y' separados por espacio")
        return [], []
    except ValueError as e:
        print(f"Error al leer los datos: {e}")
        return [], []
    
    return puntos_x, puntos_y

# Funciones auxiliares para eliminacion gaussiana
def es_casi_cero(x: float, tol: float = 1e-12) -> bool:
    """Verifica si un numero es casi cero"""
    return abs(x) < tol

def clonar_matriz(A: List[List[float]]) -> List[List[float]]:
    """Crea una copia profunda de la matriz A"""
    return [fila[:] for fila in A]

def intercambiar_filas(A: List[List[float]], b: List[float], i: int, j: int) -> None:
    """Intercambia la fila i con la fila j en la matriz A y el vector b"""
    if i == j:
        return
    A[i], A[j] = A[j], A[i]
    b[i], b[j] = b[j], b[i]

def sustitucion_atras(U: List[List[float]], y: List[float], tol: float = 1e-12) -> List[float]:
    """
    Resuelve U x = y por sustitucion hacia atras
    donde U es una matriz triangular superior
    """
    n = len(U)
    x = [0.0] * n
    
    for i in range(n-1, -1, -1):
        suma = y[i]
        for j in range(i+1, n):
            suma = suma - U[i][j] * x[j]
        
        if es_casi_cero(U[i][i], tol):
            raise ValueError("Pivote nulo en sustitucion hacia atras")
        
        x[i] = suma / U[i][i]
    
    return x

def eliminacion_gaussiana(A: List[List[float]], b: List[float], tol: float = 1e-12) -> List[float]:
    """
    Resuelve A x = b por Eliminacion Gaussiana con pivoteo parcial.
    Implementacion basada en el pseudocodigo de la clase.
    
    Parametros:
    -----------
    A : Matriz de coeficientes
    b : Vector de terminos independientes
    tol : Tolerancia para detectar valores casi cero
    
    Retorna:
    --------
    x : Solucion del sistema
    """
    n = len(A)
    
    # Verificar dimensiones
    if any(len(fila) != n for fila in A):
        raise ValueError("La matriz A debe ser cuadrada")
    if len(b) != n:
        raise ValueError("Dimension de b incompatible con A")
    
    # Crear copias para no modificar los originales
    U = clonar_matriz(A)
    c = b[:]
    
    # Eliminacion hacia adelante con pivoteo parcial
    for i in range(n-1):
        # Buscar el pivote maximo en la columna i desde la fila i hasta n-1
        p = i
        max_abs = abs(U[i][i])
        
        for l in range(i+1, n):
            if abs(U[l][i]) > max_abs:
                max_abs = abs(U[l][i])
                p = l
        
        # Verificar si el pivote es casi cero
        if es_casi_cero(max_abs, tol):
            raise ValueError("Matriz singular o casi singular (pivote ~ 0)")
        
        # Intercambiar filas si es necesario
        if p != i:
            intercambiar_filas(U, c, i, p)
        
        # Anular entradas debajo del pivote
        for j in range(i+1, n):
            # Calcular el factor multiplicador
            factor = U[j][i] / U[i][i]
            
            # Actualizar la fila j
            for k in range(i, n):
                U[j][k] = U[j][k] - factor * U[i][k]
            
            # Actualizar el vector c
            c[j] = c[j] - factor * c[i]
    
    # Verificar el ultimo pivote
    if es_casi_cero(U[n-1][n-1], tol):
        raise ValueError("Matriz singular (ultimo pivote ~ 0)")
    
    # Sustitucion hacia atras
    x = sustitucion_atras(U, c, tol)
    
    return x

def construir_matriz_A(puntos_x: List[float]) -> List[List[float]]:
    """
    Construye la matriz A para los puntos x dados.
    Segun el pseudocodigo: A[i][j] = pow(x[i], j)
    
    Parametros:
    -----------
    puntos_x : Lista de coordenadas x
    
    Retorna:
    --------
    Matriz A donde A[i][j] = x[i]^j
    """
    n = len(puntos_x)
    A = []
    
    # Para cada fila i (cada punto xi)
    for i in range(n):
        fila = []
        # Para cada columna j (cada potencia)
        for j in range(n):
            # A[i][j] = xi^j
            valor = pow(puntos_x[i], j)
            fila.append(valor)
        A.append(fila)
    
    return A

def evaluar_polinomio(coeficientes: List[float], x: float) -> float:
    """
    Evalua el polinomio con los coeficientes dados en un punto x.
    P(x) = a0 + a1*x + a2*x^2 + ... + an*x^n
    
    Parametros:
    -----------
    coeficientes : Lista con coeficientes del polinomio [a0, a1, a2, ..., an]
    x : Punto donde evaluar el polinomio
    
    Retorna:
    --------
    Valor del polinomio en x
    """
    suma = 0.0
    for i in range(len(coeficientes)):
        suma = suma + coeficientes[i] * pow(x, i)
    
    return suma

def main():
    """
    Programa principal para interpolacion por sistema de ecuaciones
    Implementacion del pseudocodigo de la clase
    """
    
    print("="*60)
    print("INTERPOLACION POLINOMIAL - SISTEMA DE ECUACIONES")
    print("="*60)
    
    # Leer los datos del archivo
    print("\nFormato del archivo: cada linea debe contener 'x y' separados por espacio")
    print("Ejemplo: datos.txt (la extension .txt se agrega automaticamente si no se especifica)")
    nombre_archivo = input("\nIngrese el nombre del archivo de datos: ")
    puntos_x, puntos_y = leer_datos(nombre_archivo)
    
    if not puntos_x:
        print("No se pudieron leer los datos del archivo")
        return
    
    n = len(puntos_x)
    
    # Mostrar los puntos leidos
    print(f"\nSe leyeron {n} puntos del archivo:")
    print("-"*40)
    for i in range(n):
        print(f"Punto {i}: x{i} = {puntos_x[i]:.4f}, y{i} = {puntos_y[i]:.4f}")
    
    # Armar la matriz A y el vector b
    print("\n" + "-"*40)
    print("Construyendo el sistema de ecuaciones...")
    
    # Construir matriz A
    A = construir_matriz_A(puntos_x)
    b = puntos_y[:]
    
    # Resolver el sistema para obtener los coeficientes
    try:
        print("Resolviendo el sistema con eliminacion gaussiana...")
        coeficientes = eliminacion_gaussiana(A, b, tol=1e-12)
    except ValueError as e:
        print(f"Error al resolver el sistema: {e}")
        return
    
    # Mostrar los coeficientes obtenidos
    print("\n" + "="*60)
    print("COEFICIENTES DEL POLINOMIO:")
    print("-"*40)
    for i in range(len(coeficientes)):
        print(f"a{i} = {coeficientes[i]:.6f}")
    
    # Construir y mostrar el polinomio
    print("\n" + "-"*40)
    print("POLINOMIO INTERPOLADOR:")
    terminos = []
    for i in range(len(coeficientes)):
        coef = coeficientes[i]
        if abs(coef) > 1e-10:  # Solo mostrar terminos significativos
            if i == 0:
                terminos.append(f"{coef:.4f}")
            elif i == 1:
                if coef > 0:
                    terminos.append(f"{coef:.4f}x")
                else:
                    terminos.append(f"({coef:.4f})x")
            else:
                if coef > 0:
                    terminos.append(f"{coef:.4f}x^{i}")
                else:
                    terminos.append(f"({coef:.4f})x^{i}")
    
    if terminos:
        polinomio = terminos[0]
        for termino in terminos[1:]:
            if termino[0] != '(':
                polinomio += " + " + termino
            else:
                polinomio += " " + termino
        print(f"P(x) = {polinomio}")
    
    # Evaluar el polinomio en un punto
    print("\n" + "-"*40)
    respuesta = input("Desea evaluar el polinomio en algun punto? (s/n): ")
    
    while respuesta.lower() == 's':
        x_eval = float(input("\nIngrese el valor de x: "))
        resultado = evaluar_polinomio(coeficientes, x_eval)
        print(f"P({x_eval}) = {resultado:.6f}")
        
        respuesta = input("\nDesea evaluar en otro punto? (s/n): ")
    
    # Verificacion: el polinomio debe pasar por todos los puntos originales
    print("\n" + "="*60)
    print("VERIFICACION:")
    print("El polinomio debe pasar exactamente por todos los puntos")
    print("-"*40)
    for i in range(n):
        y_calculado = evaluar_polinomio(coeficientes, puntos_x[i])
        error = abs(y_calculado - puntos_y[i])
        print(f"P({puntos_x[i]:.4f}) = {y_calculado:.6f}, y_real = {puntos_y[i]:.6f}, error = {error:.2e}")

# Ejecutar el programa
if __name__ == "__main__":
    main()