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

def spline_cubica(x_vals, y_vals, x):
    """Spline cubica simple (interpolacion lineal por segmentos)"""
    n = len(x_vals)
    
    # Encontrar el intervalo apropiado
    for i in range(n-1):
        if x_vals[i] <= x <= x_vals[i+1]:
            # Interpolacion lineal
            t = (x - x_vals[i]) / (x_vals[i+1] - x_vals[i])
            return y_vals[i] * (1 - t) + y_vals[i+1] * t
    
    # Si x esta fuera del rango, usar extrapolacion lineal
    if x < x_vals[0]:
        return y_vals[0]
    else:
        return y_vals[-1]
