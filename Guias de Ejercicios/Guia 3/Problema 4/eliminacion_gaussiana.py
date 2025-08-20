
def pivoteo_parcial(A, b, k):
    """
    Realiza pivoteo parcial en la columna k
    Encuentra la fila con el mayor valor absoluto en la columna k
    e intercambia con la fila k
    """
    n = len(A)
    max_val = abs(A[k][k])
    max_row = k
    
    # Buscar el maximo valor absoluto en la columna k
    for i in range(k + 1, n):
        if abs(A[i][k]) > max_val:
            max_val = abs(A[i][k])
            max_row = i
    
    # Intercambiar filas si es necesario
    if max_row != k:
        A[k], A[max_row] = A[max_row], A[k]
        b[k], b[max_row] = b[max_row], b[k]
        print(f"Intercambio: fila {k+1} <-> fila {max_row+1}")
    
    return A, b

def eliminacion_hacia_adelante(A, b):
    """
    Realiza eliminacion hacia adelante con pivoteo parcial
    Convierte la matriz A en triangular superior
    """
    n = len(A)
    
    for k in range(n - 1):
        # Aplicar pivoteo parcial
        A, b = pivoteo_parcial(A, b, k)
        
        # Verificar si el pivote es muy pequeno
        if abs(A[k][k]) < 1e-10:
            raise ValueError("Sistema singular o mal condicionado")
        
        # Eliminacion
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - factor * A[k][j]
            b[i] = b[i] - factor * b[k]
            
        # Mostrar estado intermedio
        print(f"\nPaso {k+1}:")
        mostrar_sistema(A, b)
    
    return A, b

def sustitucion_hacia_atras(A, b):
    """
    Resuelve el sistema triangular superior Ax = b
    por sustitucion hacia atras
    """
    n = len(A)
    x = [0.0] * n
    
    for i in range(n - 1, -1, -1):
        suma = b[i]
        for j in range(i + 1, n):
            suma = suma - A[i][j] * x[j]
        x[i] = suma / A[i][i]
    
    return x

def resolver_sistema(A, b):
    """
    Resuelve el sistema Ax = b usando eliminacion gaussiana
    con pivoteo parcial
    """
    n = len(A)
    
    # Copiar matrices para no modificar las originales
    A_copia = [fila[:] for fila in A]
    b_copia = b[:]
    
    print("Sistema original:")
    mostrar_sistema(A_copia, b_copia)
    
    print("\n=== ELIMINACION HACIA ADELANTE CON PIVOTEO PARCIAL ===")
    
    # Eliminacion hacia adelante
    A_triangular, b_modificado = eliminacion_hacia_adelante(A_copia, b_copia)
    
    print("\n=== SISTEMA TRIANGULAR SUPERIOR ===")
    mostrar_sistema(A_triangular, b_modificado)
    
    # Sustitucion hacia atras
    print("\n=== SUSTITUCION HACIA ATRAS ===")
    x = sustitucion_hacia_atras(A_triangular, b_modificado)
    
    return x

def mostrar_sistema(A, b):
    """
    Muestra el sistema de ecuaciones en formato matricial
    """
    n = len(A)
    for i in range(n):
        fila = " ".join(f"{A[i][j]:8.4f}" for j in range(n))
        print(f"[ {fila} ] [ x{i+1} ] = [ {b[i]:8.4f} ]")

def verificar_solucion(A, b, x):
    """
    Verifica que Ax = b para la solucion encontrada
    """
    n = len(A)
    residuo = []
    for i in range(n):
        suma = 0
        for j in range(n):
            suma += A[i][j] * x[j]
        residuo.append(abs(suma - b[i]))
    return max(residuo)