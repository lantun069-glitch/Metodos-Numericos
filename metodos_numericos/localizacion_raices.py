# Modulo de Localizacion de Raices

def calcular_error(valor_nuevo, valor_anterior, tipo='absoluto'):
    if tipo == 'absoluto':
        return abs(valor_nuevo - valor_anterior)
    elif tipo == 'relativo':
        if valor_nuevo != 0:
            return abs((valor_nuevo - valor_anterior) / valor_nuevo)
        return float('inf')
    elif tipo == 'porcentual':
        if valor_nuevo != 0:
            return abs((valor_nuevo - valor_anterior) / valor_nuevo) * 100
        return float('inf')

def verificar_cambio_signo(f, a, b):
    try:
        return f(a) * f(b) < 0
    except:
        return False

def biseccion(f, a, b, tolerancia=1e-5, tipo_error='absoluto', max_iter=100):
    if not verificar_cambio_signo(f, a, b):
        raise ValueError("No hay cambio de signo en el intervalo")
    
    iteracion = 0
    c_viejo = None
    error_final = None
    historial = []
    
    while iteracion < max_iter:
        c = (a + b) / 2
        fc = f(c)
        
        if c_viejo is not None:
            error_final = calcular_error(c, c_viejo, tipo_error)
        
        historial.append({'iteracion': iteracion + 1, 'a': a, 'b': b, 'c': c, 'fc': fc, 'error': error_final})
        
        if c_viejo is not None and error_final <= tolerancia:
            return c, fc, error_final
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        
        c_viejo = c
        iteracion += 1
    
    return c, f(c), error_final

def newton_raphson(f, df, x0, tolerancia=1e-5, tipo_error='absoluto', max_iter=100):
    x = x0
    historial = []
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-12:
            return None, None, historial
        
        x_nuevo = x - fx / dfx
        error = calcular_error(x_nuevo, x, tipo_error) if i > 0 else None
        
        historial.append({'iteracion': i + 1, 'x': x, 'fx': fx, 'x_nuevo': x_nuevo, 'error': error})
        
        if i > 0 and error <= tolerancia:
            return x_nuevo, f(x_nuevo), error
        
        x = x_nuevo
    
    return x, f(x), error

def regula_falsi(f, a, b, tolerancia=1e-5, tipo_error='absoluto', max_iter=100):
    if not verificar_cambio_signo(f, a, b):
        raise ValueError("No hay cambio de signo en el intervalo")
    
    iteracion = 0
    c_viejo = None
    error_final = None
    historial = []
    
    while iteracion < max_iter:
        fa = f(a)
        fb = f(b)
        
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        
        if c_viejo is not None:
            error_final = calcular_error(c, c_viejo, tipo_error)
        
        historial.append({'iteracion': iteracion + 1, 'a': a, 'b': b, 'c': c, 'fc': fc, 'error': error_final})
        
        if c_viejo is not None and error_final <= tolerancia:
            return c, fc, error_final
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        
        c_viejo = c
        iteracion += 1
    
    return c, f(c), error_final

def punto_fijo(g, x0, tolerancia=1e-5, tipo_error='absoluto', max_iter=100):
    x = x0
    historial = []
    
    for i in range(max_iter):
        x_nuevo = g(x)
        error = calcular_error(x_nuevo, x, tipo_error) if i > 0 else None
        
        historial.append({'iteracion': i + 1, 'x': x, 'g_x': x_nuevo, 'error': error})
        
        if i > 0 and error <= tolerancia:
            return x_nuevo, error
        
        x = x_nuevo
    
    return x, error

def secante(f, x0, x1, tolerancia=1e-5, tipo_error='absoluto', max_iter=100):
    historial = []
    
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        
        if abs(fx1 - fx0) < 1e-12:
            return None, None, historial
        
        x_nuevo = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = calcular_error(x_nuevo, x1, tipo_error) if i > 0 else None
        
        historial.append({'iteracion': i + 1, 'x0': x0, 'x1': x1, 'x_nuevo': x_nuevo, 'error': error})
        
        if i > 0 and error <= tolerancia:
            return x_nuevo, f(x_nuevo), error
        
        x0, x1 = x1, x_nuevo
    
    return x1, f(x1), error
