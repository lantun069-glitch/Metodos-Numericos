from funciones import g, calcular_error

def punto_fijo(x0, tolerancia=1e-3, max_iter=50):
    x = x0
    
    for i in range(max_iter):
        x_nuevo = g(x)
        error = calcular_error(x_nuevo, x, 'absoluto')
        
        print(f"Iter {i+1}: x = {x:.6f}, g(x) = {x_nuevo:.6f}, Error = {error:.6f}")
        
        if error <= tolerancia:
            return x_nuevo
        
        x = x_nuevo
    
    return None