from funciones import f, df_dx, calcular_error

def newton_raphson(x0, tolerancia=1e-6, max_iter=50):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df_dx(x)
        
        if abs(dfx) < 1e-10:
            return None
            
        x_nuevo = x - fx / dfx
        error = calcular_error(x_nuevo, x, 'absoluto')
        
        if error <= tolerancia:
            return x_nuevo
            
        x = x_nuevo
    
    return x