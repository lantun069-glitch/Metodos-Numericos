from funciones import f, df_dx, calcular_error

def newton_raphson(x0, tolerancia=1e-9, tipo_error='absoluto', max_iter=100):
    print(f"Metodo Newton-Raphson")
    print(f"Valor inicial: x0 = {x0}")
    print(f"Tolerancia: {tolerancia}")
    
    x = x0
    iteracion = 0
    
    while iteracion < max_iter:
        fx = f(x)
        dfx = df_dx(x)
        
        if abs(dfx) < 1e-12:
            print("ERROR: Derivada muy pequeña")
            return None
        
        x_nuevo = x - fx / dfx
        error = calcular_error(x_nuevo, x, tipo_error)
        
        print(f"Iteracion {iteracion + 1}: x = {x_nuevo:.9f}, Error = {error:.2e}")
        
        if error <= tolerancia:
            print(f"Convergencia alcanzada")
            return x_nuevo
        
        x = x_nuevo
        iteracion += 1
    
    print("Maximo de iteraciones alcanzado")
    return x