from funciones import f, calcular_error

def regula_falsi(a, b, tolerancia=1e-3, tipo_error='absoluto', max_iter=100):
    if f(a) * f(b) >= 0:
        return None
    
    iteracion = 0
    c_viejo = None
    
    while iteracion < max_iter:
        c = a - f(a) * (b - a) / (f(b) - f(a))
        
        if c_viejo is not None:
            error = calcular_error(c, c_viejo, tipo_error)
            if error <= tolerancia:
                return c
        
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c
        
        c_viejo = c
        iteracion += 1
    
    return c