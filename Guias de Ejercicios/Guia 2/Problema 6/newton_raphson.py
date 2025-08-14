from funciones import f, df_dx, calcular_error

def newton_raphson(x0, tolerancia=1e-4, tipo_error='absoluto', max_iter=50):
    print(f"Iter\t\td\t\tf(d)\t\tError")
    print("-" * 45)
    
    x = x0
    error = float('inf')
    i = 0
    
    while error > tolerancia and i < max_iter:
        fx = f(x)
        dfx = df_dx(x)
        
        if abs(dfx) < 1e-10:
            print("ERROR: Derivada muy pequena")
            return None
        
        x_nuevo = x - fx / dfx
        
        if x_nuevo < 0:
            x_nuevo = 0.1
        elif x_nuevo > 20:
            x_nuevo = 19.9
        
        error = calcular_error(x_nuevo, x, tipo_error) if i > 0 else float('inf')
        
        print(f"{i+1}\t\t{x:.6f}\t{fx:.6f}\t{error:.6f}")
        
        x = x_nuevo
        i += 1
    
    return x