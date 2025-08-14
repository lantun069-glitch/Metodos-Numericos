from funciones import calcular_error

def punto_fijo(g_func, x0, tolerancia=1e-12, max_iter=100):
    x = x0
    
    for i in range(max_iter):
        try:
            x_nuevo = g_func(x)
            error = calcular_error(x_nuevo, x, 'absoluto')
            
            if error <= tolerancia:
                return x_nuevo
            
            x = x_nuevo
            
        except:
            return None
    
    return None