from funciones import f, df_dx, calcular_error

def newton_raphson(x0, tolerancia=1e-3, tipo_error='absoluto', max_iter=100, mostrar_iteraciones=True):
    """
    Metodo de Newton-Raphson para encontrar raices
    
    Args:
        x0: Valor inicial
        tolerancia: Tolerancia para el error
        tipo_error: 'absoluto' o 'porcentual'
        max_iter: Numero máximo de iteraciones
        mostrar_iteraciones: Si mostrar el proceso iterativo
    
    Returns:
        La raiz encontrada o None si no converge
    """
    print(f"\n=== METODO DE NEWTON-RAPHSON ===")
    print(f"Valor inicial: x0 = {x0}")
    print(f"Tolerancia: {tolerancia}")
    print(f"Tipo de error: {tipo_error}")
    
    unidad_error = "%" if tipo_error == 'porcentual' else ""
    
    if mostrar_iteraciones:
        print(f"\n{'Iter':<4} {'x':<12} {'f(x)':<12} {'f\'(x)':<12} {'Error':<12}")
        print("-" * 60)
    
    i = 0
    x = x0
    error = float('inf')
    
    while error > tolerancia and i < max_iter:
        fx = f(x)
        dfx = df_dx(x)
        
        # Verificar que la derivada no sea cero
        if abs(dfx) < 1e-10:
            print("ERROR: Derivada muy chica, el metodo no converge")
            return None

        # Calcular nueva aproximacion
        x_nuevo = x - fx / dfx
        error = calcular_error(x_nuevo, x, tipo_error)
        
        if mostrar_iteraciones:
            print(f"{i+1:<4} {x:<12.6f} {fx:<12.6f} {dfx:<12.6f} {error:<12.6f}{unidad_error}")
        
        x = x_nuevo
        i += 1
    
    print(f"\n=== RESULTADOS ===")
    print(f"Raiz encontrada: x = {x:.8f}")
    print(f"f({x:.8f}) = {f(x):.8f}")
    print(f"Error final: {error:.8f}{unidad_error}")
    print(f"Numero de iteraciones: {i}")
    print(f"Tolerancia requerida: {tolerancia}{unidad_error}")
    
    if error <= tolerancia:
        return x
    else:
        print("ERROR: No se alcanzo la tolerancia en el numero maximo de iteraciones")
        return None
