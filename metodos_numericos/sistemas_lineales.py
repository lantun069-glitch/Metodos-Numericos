# Modulo de Sistemas Lineales

def eliminacion_gaussiana(A, b):
    """Eliminacion gaussiana con pivoteo parcial"""
    n = len(A)
    
    # Copiar matrices para no modificar originales
    A_copy = [fila[:] for fila in A]
    b_copy = b[:]
    
    # Eliminacion hacia adelante
    for k in range(n):
        # Pivoteo parcial
        max_fila = k
        for i in range(k+1, n):
            if abs(A_copy[i][k]) > abs(A_copy[max_fila][k]):
                max_fila = i
        
        # Intercambiar filas
        A_copy[k], A_copy[max_fila] = A_copy[max_fila], A_copy[k]
        b_copy[k], b_copy[max_fila] = b_copy[max_fila], b_copy[k]
        
        # Eliminacion
        for i in range(k+1, n):
            if A_copy[k][k] != 0:
                factor = A_copy[i][k] / A_copy[k][k]
                for j in range(k, n):
                    A_copy[i][j] -= factor * A_copy[k][j]
                b_copy[i] -= factor * b_copy[k]
    
    # Sustitucion hacia atras
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b_copy[i]
        for j in range(i+1, n):
            x[i] -= A_copy[i][j] * x[j]
        x[i] /= A_copy[i][i]
    
    return x

def jacobi(A, b, x0=None, tolerancia=1e-5, max_iter=100):
    """Metodo de Jacobi para sistemas lineales"""
    n = len(A)
    if x0 is None:
        x0 = [0] * n
    
    x = x0[:]
    x_nuevo = [0] * n
    
    for iteracion in range(max_iter):
        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    suma += A[i][j] * x[j]
            x_nuevo[i] = (b[i] - suma) / A[i][i]
        
        # Calcular error
        error = max(abs(x_nuevo[i] - x[i]) for i in range(n))
        
        if error < tolerancia:
            return x_nuevo, iteracion + 1
        
        x = x_nuevo[:]
    
    return x, max_iter

def gauss_seidel(A, b, x0=None, tolerancia=1e-5, max_iter=100):
    """Metodo de Gauss-Seidel para sistemas lineales"""
    n = len(A)
    if x0 is None:
        x0 = [0] * n
    
    x = x0[:]
    
    for iteracion in range(max_iter):
        x_viejo = x[:]
        
        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    suma += A[i][j] * x[j]
            x[i] = (b[i] - suma) / A[i][i]
        
        # Calcular error
        error = max(abs(x[i] - x_viejo[i]) for i in range(n))
        
        if error < tolerancia:
            return x, iteracion + 1
    
    return x, max_iter

def relajacion(A, b, x0=None, omega=1.25, tolerancia=1e-5, max_iter=100):
    """Metodo de relajacion (SOR)"""
    n = len(A)
    if x0 is None:
        x0 = [0] * n
    
    x = x0[:]
    
    for iteracion in range(max_iter):
        x_viejo = x[:]
        
        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    suma += A[i][j] * x[j]
            x_gs = (b[i] - suma) / A[i][i]
            x[i] = (1 - omega) * x[i] + omega * x_gs
        
        # Calcular error
        error = max(abs(x[i] - x_viejo[i]) for i in range(n))
        
        if error < tolerancia:
            return x, iteracion + 1
    
    return x, max_iter
