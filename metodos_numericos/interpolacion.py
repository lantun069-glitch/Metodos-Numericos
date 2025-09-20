# Modulo de Interpolacion

def sistema_ecuaciones(x_vals, y_vals):
    """Resuelve un sistema de ecuaciones para interpolacion polinomial"""
    n = len(x_vals)
    
    # Crear matriz de Vandermonde
    A = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(x_vals[i] ** j)
        A.append(fila)
    
    # Resolver por eliminacion gaussiana
    coeficientes = eliminacion_gaussiana_simple(A, y_vals)
    
    # Crear funcion polinomial
    def polinomio(x):
        resultado = 0
        for i, coef in enumerate(coeficientes):
            resultado += coef * (x ** i)
        return resultado
    
    return coeficientes, polinomio

def eliminacion_gaussiana_simple(A, b):
    """Eliminacion gaussiana simple para resolver Ax = b"""
    n = len(A)
    
    # Crear matriz aumentada
    for i in range(n):
        A[i].append(b[i])
    
    # Eliminacion hacia adelante
    for k in range(n):
        # Pivoteo parcial
        max_fila = k
        for i in range(k+1, n):
            if abs(A[i][k]) > abs(A[max_fila][k]):
                max_fila = i
        A[k], A[max_fila] = A[max_fila], A[k]
        
        # Eliminacion
        for i in range(k+1, n):
            if A[k][k] != 0:
                factor = A[i][k] / A[k][k]
                for j in range(k, n+1):
                    A[i][j] -= factor * A[k][j]
    
    # Sustitucion hacia atras
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    
    return x

def lagrange(x_vals, y_vals, x):
    """Interpolacion de Lagrange"""
    n = len(x_vals)
    resultado = 0
    
    for i in range(n):
        termino = y_vals[i]
        for j in range(n):
            if i != j:
                termino *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        resultado += termino
    
    return resultado

def cuadrados_minimos(x_vals, y_vals, grado):
    """Regresion por cuadrados minimos"""
    n = len(x_vals)
    m = grado + 1
    
    # Crear matriz normal
    A = []
    for i in range(m):
        fila = []
        for j in range(m):
            suma = sum(x_vals[k] ** (i + j) for k in range(n))
            fila.append(suma)
        A.append(fila)
    
    # Vector b
    b = []
    for i in range(m):
        suma = sum(y_vals[k] * (x_vals[k] ** i) for k in range(n))
        b.append(suma)
    
    # Resolver sistema
    coeficientes = eliminacion_gaussiana_simple(A, b)
    
    def polinomio(x):
        resultado = 0
        for i, coef in enumerate(coeficientes):
            resultado += coef * (x ** i)
        return resultado
    
    return coeficientes, polinomio

def spline_cubica(xv, yv, x):
    """
    Spline cubica natural 1D.
    xv: nodos en orden creciente (len n >= 2)
    yv: valores en cada nodo
    x : punto a evaluar
    return: S(x)
    """
    n = len(xv)
    if n != len(yv) or n < 2:
        raise ValueError("xv y yv deben tener misma longitud y n>=2")
    # verificar que xv sea estrictamente creciente
    for i in range(n-1):
        if xv[i] >= xv[i+1]:
            raise ValueError("xv debe ser estrictamente creciente")

    # paso 1: armar sistema tridiagonal para segundas derivadas M
    h = [xv[i+1] - xv[i] for i in range(n-1)]

    # diagonales de la matriz (condicion natural: extremos fijos)
    a = [0.0] + h[:-1]                              # subdiagonal
    b = [1.0] + [2.0*(h[i-1]+h[i]) for i in range(1, n-1)] + [1.0]  # diagonal
    c = h[1:] + [0.0]                               # superdiagonal

    # lado derecho del sistema (extremos en 0 por condicion natural)
    d = [0.0]*n
    for i in range(1, n-1):
        d[i] = 6.0 * ((yv[i+1]-yv[i]) / h[i] - (yv[i]-yv[i-1]) / h[i-1])

    # paso 2: resolver A*M = d con algoritmo de Thomas
    # eliminacion hacia adelante
    for i in range(1, n):
        w = a[i] / b[i-1]
        b[i] -= w * c[i-1]
        d[i] -= w * d[i-1]
    # sustitucion hacia atras
    M = [0.0]*n
    M[-1] = d[-1] / b[-1]
    for i in range(n-2, -1, -1):
        M[i] = (d[i] - c[i]*M[i+1]) / b[i]

    # paso 3: localizar el intervalo [x_i, x_{i+1}]
    if x <= xv[0]:
        i = 0                  # extrapolacion simple con primer tramo
    elif x >= xv[-1]:
        i = n-2                # ultimo tramo
    else:
        i = 0
        while not (xv[i] <= x <= xv[i+1]):
            i += 1

    # paso 4: evaluar la spline en el intervalo
    xi, xi1 = xv[i], xv[i+1]
    hi = xi1 - xi
    yi, yi1 = yv[i], yv[i+1]
    Mi, Mi1 = M[i], M[i+1]

    A = (xi1 - x) / hi
    B = (x - xi) / hi
    S = (A*yi + B*yi1
         + ((A**3 - A) * (hi**2) * Mi) / 6.0
         + ((B**3 - B) * (hi**2) * Mi1) / 6.0)
    return S
